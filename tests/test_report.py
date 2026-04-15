from pipeline.schema.preprocessed import PrepModelsSchema, PrepPoliciesSchema
from pipeline.schema.report import AverageCarVolumeSchema
from pipeline.report import find_average_car_volume_by_age
import polars as pl
from polars.testing import assert_frame_equal


def test_find_average_car_volume_by_age():
    # Arrange
    models = PrepModelsSchema.sample(
        overrides=[
            {"model": "M1", "height": 1_500, "width": 2_000, "length": 2_500},
            {"model": "M2", "height": 2_000, "width": 2_000, "length": 2_000},
        ]
    )
    # TODO: Use `.sample` to create a policies dataframe with two policies:
    # One with model "M1" and car age 4.5,
    # One with model "M2" and car age 14.5
    policies = PrepPoliciesSchema.sample(...)

    volume_m1 = 1e-9 * 1_500 * 2_000 * 2_500
    volume_m2 = 1e-9 * 2_000 * 2_000 * 2_000
    change = 100 * (volume_m2 / volume_m1 - 1)
    expected = AverageCarVolumeSchema.validate(
        # TODO: Add the second, missing row for the expected dataframe
        pl.DataFrame(
            [{"age_of_car": "(-inf, 10]", "volume": volume_m1, "change": None}, ...]
        ),
        cast=True,
    ).lazy()

    # Act
    df = find_average_car_volume_by_age(models, policies)

    # Assert
    assert_frame_equal(expected, df)
