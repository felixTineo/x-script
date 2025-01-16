import tweepy
import setup

bearer_oauth = setup.BEARER_TOKEN
api_key = setup.API_KEY
api_secret = setup.API_SECRET
access_token = setup.ACCESS_TOKEN
access_token_secret = setup.ACCESS_TOKEN_SECRET
client_id = setup.CLIENT_ID
client_secret = setup.CLIENT_SECRET

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
