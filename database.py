import setup
import redis

r = redis.Redis(
    host=setup.REDIS_HOST,
    port=setup.REDIS_PORT,
    decode_responses=True,
    username=setup.REDIS_USERNAME,
    password=setup.REDIS_PASSWORD,
)
