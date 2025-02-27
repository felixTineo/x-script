from newsdataapi import NewsDataApiClient
import config

url = f"{config.NEWS_API_URL}/{config.NEWS_API_VERSION}/latest"
api = NewsDataApiClient(apikey=config.NEWS_API_KEY)


def get() -> list:
    response = api.news_api(category="politics", country="ve")
    return response["results"]
    # return [
    #     {
    #         "title": "Maduro crea una comisión para impulsar una reforma a la Constitución de Venezuela",
    #         "link": "https://cnnespanol.cnn.com/2025/01/15/venezuela/maduro-crea-comision-reforma-constitucion-orix",
    #         "keywords": ["venezuela", "politica"],
    #         "article_id": "1",
    #     }
    # ]
