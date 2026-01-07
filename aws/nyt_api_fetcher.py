import os
import json
from urllib.request import urlopen
from urllib.parse import urlencode
from common.contracts import DataFetcher, Headline

class NYTAPIFetcher(DataFetcher):
    def __init__(self):
        self.api_key = os.environ["NYT_API_KEY"]
        self.base_url = "https://api.nytimes.com/svc/topstories/v2/home.json"

    def fetch(self) -> list[Headline]:
        query_string = urlencode({"api-key": self.api_key})
        url = f"{self.base_url}?{query_string}"

        with urlopen(url, timeout=10) as response:
            if response.status != 200:
                raise RuntimeError(f"NYT API request failed with status {response.status}")

            data = json.loads(response.read().decode("utf-8"))

        headlines = []
        for item in data.get("results", []):
            headlines.append(
                Headline(
                    title=item.get("title", ""),
                    url=item.get("url", "")
                )
            )

        return headlines
