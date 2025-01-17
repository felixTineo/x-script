import config
import redis


def connect_to_redis():
    return redis.Redis(
        host=config.REDIS_HOST,
        port=config.REDIS_PORT,
        decode_responses=True,
        username=config.REDIS_USERNAME,
        password=config.REDIS_PASSWORD,
        db=0,
    )


def disconnect_from_redis(redis_instance: redis.Redis):
    if redis_instance:
        try:
            redis_instance.close()
        except Exception as e:
            print("Error al cerrar la conexión de Redis:", e)
