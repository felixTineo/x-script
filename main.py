import news
import ai
import tweet

try:
    daily_news = news.get()
    ai_comment = ai.generate_ai_comment(daily_news[0]["title"])
    text = ai_comment if ai_comment else daily_news[0]["title"]
    link = daily_news[0]["link"] if daily_news[0]["link"] else ""
    post = f"{text} \n{link}"
    print("POST:", post)
    tags = daily_news[0]["tags"]
    result = tweet.post(post, [])
    print(result)
except Exception as e:
    print(e)
