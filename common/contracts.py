from dataclasses import dataclass

@dataclass
class Headline:
    title: str
    url: str

@dataclass
class HeadlineStats:
    latest_title: str
    latest_url: str

    def to_dictionary(self):
        return {
            "latest_title": self.latest_title,
            "latest_url": self.latest_url
        }

class DataFetcher:
    def fetch(self) -> list[Headline]:
        raise NotImplementedError

class DataProcessor:
    def compute_latest(self, headlines: list[Headline]) -> HeadlineStats:
        raise NotImplementedError

def read_and_compute(fetcher: DataFetcher, processor: DataProcessor) -> HeadlineStats:
    data = fetcher.fetch()
    return processor.compute_latest(data)
