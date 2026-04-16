import polars as pl
import polars.selectors as cs

from ._internal import Report
from .data import PreprocessedData


def build_report(prep: PreprocessedData) -> Report:
    return Report(
        popularity=find_three_most_popular_make_and_models(prep.models, prep.policies),
        safety=find_safest_models(prep.models),
        volume=find_average_car_volume_by_age(prep.models, prep.policies),
    )


def find_three_most_popular_make_and_models[T: (pl.DataFrame, pl.LazyFrame)](
    models: T, policies: T
) -> T:
    """Among all policies, compute the three make/model combinations that appears most often.

    Returns:
        A dataframe with three rows and three columns (make, model, count).
    """
    return (
        policies.join(models.select("model", "make"), on="model", how="inner")
        .group_by("make", "model")
        .len()
        .sort("len", descending=True)
        .head(3)
        .rename({"len": "count"})
    )


def find_safest_models[T: (pl.DataFrame, pl.LazyFrame)](models: T) -> T:
    """Among all models, find the safest ones as measured by the number of safety features.

    Returns:
        A data frame with five rows and three columns (model, segment, safety_score).
    """
    safety_score = pl.sum_horizontal(cs.starts_with("is_").cast(pl.UInt8)) + pl.col(
        "airbags"
    ).cast(pl.UInt16)
    return (
        models.select("model", "segment", safety_score=safety_score)
        .sort("safety_score", descending=True)
        .head(5)
    )


def find_average_car_volume_by_age[T: (pl.DataFrame, pl.LazyFrame)](
    models: T, policies: T
) -> T:
    """Among all policies, find the mean physical car volume in 10-year blocks of car age.

    This method should compute the volume of a car if interpreted as cuboid (i.e. box-shaped).
    Blocks should be 0-10 years, 10-20 years, etc.

    Returns:
        A data frame with three columns (age block, mean volume in cubic meters,
        relative change of mean volume relative to the previous age block in percent).
    """
    dims = models.select("model", "length", "width", "height")
    volume_m3 = (
        pl.col("length").cast(pl.Float64)
        * pl.col("width").cast(pl.Float64)
        * pl.col("height").cast(pl.Float64)
        * 1e-9
    )
    age_bins = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0]
    joined = policies.join(dims, on="model", how="inner").with_columns(
        volume=volume_m3,
        age_of_car=pl.col("age_of_car").cut(age_bins),
    )
    by_age = joined.group_by("age_of_car").agg(pl.col("volume").mean())
    return by_age.sort("age_of_car").with_columns(
        change=(100 * (pl.col("volume") / pl.col("volume").shift(1) - 1)),
    )
