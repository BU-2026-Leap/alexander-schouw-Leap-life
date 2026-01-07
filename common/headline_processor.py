from common.contracts import DataProcessor, Headline, HeadlineStats

class HeadlineProcessor(DataProcessor):
    def compute_latest(self, headlines: list[Headline]) -> HeadlineStats:
        if not headlines:
            return HeadlineStats("No headlines available", "")

        latest = headlines[0]
        return HeadlineStats(
            latest_title=latest.title,
            latest_url=latest.url
        )
