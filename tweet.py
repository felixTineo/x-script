import tweepy
import config

bearer_oauth = config.BEARER_TOKEN
api_key = config.API_KEY
api_secret = config.API_SECRET
access_token = config.ACCESS_TOKEN
access_token_secret = config.ACCESS_TOKEN_SECRET
client_id = config.CLIENT_ID
client_secret = config.CLIENT_SECRET

auth = tweepy.OAuthHandler(client_id, client_secret)
auth.set_access_token(
    api_key,
    api_secret,
)

client = tweepy.Client(
    bearer_token=bearer_oauth,
    access_token=access_token,
    access_token_secret=access_token_secret,
    consumer_key=api_key,
    consumer_secret=api_secret,
)


def post(text: str, tags: list) -> dict:
    try:
        tags_formateados = " ".join([f"#{tag}" for tag in tags]) if tags else ""
        tweet = f"{text} {tags_formateados}"
        print(f"Publicando tweet: {tweet}")
        result = client.create_tweet(text=tweet)
        return result
    except Exception as e:
        print(f"Error al publicar el tweet: {e}")
