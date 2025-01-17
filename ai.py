from setup import GEMINI_API_KEY
import google.generativeai as genai

positive = [
    "Edmundo Gonzalez",
    "Maria Corina Machado",
]
negative = [
    "Asamblea Nacional",
    "Nicolás Maduro",
    "Diosdado Cabello",
    "Jorge Rodríguez",
    "Tareck El Aissami",
    "Delcy Rodríguez",
    "Vladimir Padrino López",
    "Chavismo",
    "PSUV",
    "Chavez",
]
role = f"tomando en cuenta que Edmundo Gonzalez y Maria Corina Machado son los lideres de la opcisión a la que pertenezco, debes ser muy positivo si en el titular aparece {' '.join(positive)}, si aparece {' '.join(negative)} debes ser muy negativo, si no aparecen {' '.join(positive)} excluyelos del tweet, crea un solo tweet como opositor venezolano de este titular: "
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_ai_comment(new: str) -> str:
    response = model.generate_content(role + new)
    return response.text
