import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def get_api_response(prompt: str) -> str | None:
    text: str | None = None

    try:
        response: dict = openai.Completion.create(model = 'text-davinci-003', prompt = prompt, temperature = 0.9, max_tokens = 150, top_p = 1, frequency_penalty = 0, presence_penalty = 0.6 , stop = ['Human:','AI:'])
        choices: dict = response.get('choices')[0]
        text = choices.get('text')

    except Exception as e:
        print("Error:", e)
    
    return text

print(get_api_response("Hi!"))
