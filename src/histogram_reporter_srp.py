from collections import Counter
from pathlib import Path


class FileReader:
    @staticmethod
    def read_file(path: str) -> list[str]:
        return list(Path(path).read_text().replace("\n", ""))


class Printer:
    def __init__(self, symbol="#"):
        self.symbol = symbol

    def print_histogram(self, histogram: list[tuple]):
        for k, v in histogram:
            print(f"{k:^3}: {self.symbol * v}")


class HistogramReporterSRP:
    def __init__(self, reader, printer, top_n=10):
        self.reader = reader
        self.printer = printer
        self.top_n = top_n

    def process(self, *paths: str):
        hist = Counter()
        for path in paths:
            tokens = self.reader.read_file(path)
            hist.update(tokens)
        self.printer.print_histogram(hist.most_common(self.top_n))
