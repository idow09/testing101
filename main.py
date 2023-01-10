from src.histogram_reporter import HistogramReporter
from src.histogram_reporter_srp import HistogramReporterSRP, Printer, FileReader


def regular():
    HistogramReporter(top_n=30, symbol="~").process("resources/sample_data.txt")


def srp():
    HistogramReporterSRP(
        reader=FileReader(),
        printer=Printer(symbol="~"),
        top_n=30,
    ).process("resources/sample_data.txt")


if __name__ == "__main__":
    regular()
    # srp()
