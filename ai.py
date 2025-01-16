from setup import GEMINI_API_KEY
import google.generativeai as genai

role = "crea u tweet como opositor venezolano de este titular: "
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_ai_comment(new: str) -> str:
    response = model.generate_content(role + new)
    return response.text
