from collections import Counter
from pathlib import Path


def read_file(path: str) -> list[str]:
    return list(Path(path).read_text().replace("\n", ""))


def print_histogram(histogram: list[tuple], symbol):
    for k, v in histogram:
        print(f"{k:^3}: {symbol * v}")


class HistogramReporterSRPPatch:
    def __init__(self, top_n=10, symbol="#"):
        self.top_n = top_n
        self.symbol = symbol

    def process(self, *paths: str):
        hist = Counter()
        for path in paths:
            tokens = read_file(path)
            hist.update(tokens)
        print_histogram(hist.most_common(self.top_n), symbol=self.symbol)
