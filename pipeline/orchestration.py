from .data import RawData
from .report import Report, build_report
from .preprocess import preprocess


def run_pipeline(raw: RawData) -> Report:
    prep = preprocess(raw)
    report = build_report(prep)
    return report
