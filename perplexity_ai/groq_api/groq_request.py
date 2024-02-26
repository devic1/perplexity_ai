from groq import Groq
from .system_template import system_template
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

def groq_request(rag_context: str,query: str) -> str:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system_template.format(rag_context)
            },
            {
                "role": "user",
                "content": query,
            }
        ],
        model="mixtral-8x7b-32768",
        )
    print(chat_completion.choices[0].message.content)
    return chat_completion.choices[0].message.content

