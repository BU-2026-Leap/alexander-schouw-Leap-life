from aws.nyt_api_fetcher import NYTAPIFetcher
from common.headline_processor import HeadlineProcessor
from common.contracts import read_and_compute

def build_html(stats):
    return f"""
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="UTF-8">
        <title>Latest NYT Headline</title>
      </head>
      <body>
        <h1>🗞 Latest New York Times Headline</h1>
        <h2>{stats.latest_title}</h2>
        <p><a href="{stats.latest_url}">Read full article</a></p>
      </body>
    </html>
    """

def lambda_handler(event, context):
    result = read_and_compute(
        NYTAPIFetcher(),
        HeadlineProcessor()
    )

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": build_html(result)
    }
