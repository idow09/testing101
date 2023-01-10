from collections import Counter
from pathlib import Path


class HistogramReporter:
    def __init__(self, top_n=10, symbol="#"):
        self.top_n = top_n
        self.symbol = symbol

    def process(self, *paths):
        hist = Counter()

        for path in paths:
            tokens = list(Path(path).read_text().replace("\n", ""))
            hist.update(tokens)

        res = [f"{k:^3}: {self.symbol * v}" for k, v in hist.most_common(self.top_n)]
        print("\n".join(res))
