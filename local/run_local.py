from local.local_json_fetcher import LocalJSONFetcher
from common.headline_processor import HeadlineProcessor
from common.contracts import read_and_compute

result = read_and_compute(
    LocalJSONFetcher("sample_nyt.json"),
    HeadlineProcessor()
)

print(result.to_dictionary())


