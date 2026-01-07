import json
from common.contracts import DataFetcher, Headline

class LocalJSONFetcher(DataFetcher):
    def __init__(self, path):
        self.path = path

    def fetch(self) -> list[Headline]:
        with open(self.path) as f:
            data = json.load(f)

        return [
            Headline(title=item["title"], url=item["url"])
            for item in data
        ]
