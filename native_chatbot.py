import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def main():
    prompt = input("Input: ")
    response: dict = openai.Completion.create(model = 'text-davinci-003', prompt = prompt, temperature = 0.9, max_tokens = 150, top_p = 1, frequency_penalty = 0, presence_penalty = 0.6 , stop = ['Human:','AI:'])
    choices: dict = response.get('choices')[0]
    text = choices.get('text')
    print(f"\nRESPONSE: {text}")
    
if __name__ == '__main__':
    main()
