import polars as pl

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
    # TODO: Implement this function
    return pl.DataFrame()


def find_safest_models[T: (pl.DataFrame, pl.LazyFrame)](models: T) -> T:
    """Among all models, find the safest ones as measured by the number of safety features.

    Returns:
        A data frame with five rows and three columns (model, segment, safety_score).
    """
    # TODO: Implement this function
    return pl.DataFrame()


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
    # TODO: Implement this function.
    # Tip: Pay attention to numeric data types when performing calculations
    # Tip: Consider https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.cut.html
    return pl.DataFrame()
