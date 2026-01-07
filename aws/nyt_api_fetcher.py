import os
import requests
from common.contracts import DataFetcher, Headline

class NYTAPIFetcher(DataFetcher):
    def __init__(self):
        self.api_key = os.environ["NYT_API_KEY"]
        self.url = "https://api.nytimes.com/svc/topstories/v2/home.json"

    def fetch(self) -> list[Headline]:
        response = requests.get(
            self.url,
            params={"api-key": self.api_key},
            timeout=10
        )
        response.raise_for_status()
        data = response.json()

        headlines = []
        for item in data["results"]:
            headlines.append(
                Headline(
                    title=item["title"],
                    url=item["url"]
                )
            )

        return headlines
