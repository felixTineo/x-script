import setup
import redis


def connect_to_redis():
    return redis.Redis(
        host=setup.REDIS_HOST,
        port=setup.REDIS_PORT,
        decode_responses=True,
        username=setup.REDIS_USERNAME,
        password=setup.REDIS_PASSWORD,
        db=0,
    )


def disconnect_from_redis(redis_instance: redis.Redis):
    if redis_instance:
        try:
            redis_instance.close()
        except Exception as e:
            print("Error al cerrar la conexión de Redis:", e)
