from dataclasses import dataclass

import polars as pl


@dataclass
class RawData[T: (pl.DataFrame | pl.LazyFrame)]:
    models: T
    policies: T


@dataclass
class PreprocessedData[T: (pl.DataFrame | pl.LazyFrame)]:
    models: T
    policies: T
