import sys
import news
import ai
import tweet
from database import connect_to_redis, disconnect_from_redis

# Conexión a Redis
redis = connect_to_redis()

try:
    # Obtener noticias
    daily_news = news.get()
    if not daily_news:
        raise ValueError("No se obtuvieron noticias.")
except Exception as e:
    print("Get news error: ", e)
    sys.exit(1)

current_new = None

try:
    # Iterar sobre las noticias
    for new in daily_news:
        if redis.exists(new["article_id"]):
            continue
        else:
            # Guardar en Redis y establecer TTL
            redis.set(new["article_id"], 1)
            redis.expire(new["article_id"], 86400)  # Expiración de 1 día
            current_new = new
            break

    # Si no se encontró una noticia nueva
    if not current_new:
        raise ValueError("No hay noticias nuevas para procesar.")

    print("Noticia procesada:", current_new)
except Exception as e:
    print("Check news error: ", e)
    disconnect_from_redis(redis)
    sys.exit(1)

finally:
    disconnect_from_redis(redis)

try:
    ai_comment = ai.generate_ai_comment(current_new["title"])
    text = ai_comment if ai_comment else current_new["title"]
    link = current_new["link"] if current_new["link"] else ""
    post = f"{text} \n{link}"
    print("POST:", post)
    # result = tweet.post(post, [])
    # print("Resultado del tweet:", result)

except Exception as e:
    print("Error al procesar la noticia o generar el post:", e)
