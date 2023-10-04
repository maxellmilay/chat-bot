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

def update_list(message: str, prompt_list: list[str]):
    prompt_list.append(message)

def create_prompt(message: str, prompt_list: list[str]) -> str:
    processed_message: str = f'\nHuman: {message}'
    update_list(processed_message, prompt_list)
    prompt: str = ''.join(prompt_list)

    return prompt

def get_bot_response(message: str, prompt_list: list[str]) -> str:
    prompt: str = create_prompt(message, prompt_list)
    bot_response: str = get_api_response(prompt)

    if bot_response:
        update_list(bot_response,prompt_list)
        position: int = bot_response.find('\nAI: ')
        bot_response = bot_response[position + 5:]
    else:
        bot_response = 'Something went wrong...'
    
    return bot_response

def main():
    prompt_list: list[str] = ['You are a low ranking officer in the army that ends every response with "Sir!"',
                              '\nHuman: How was the mission?',
                              '\nAI: The hostages were successfully rescued, Sir!']

    while True:
        user_input: str = input('You: ')
        response: str = get_bot_response(user_input,prompt_list)
        print(f'Bot: {response}')
    
    

if __name__ == '__main__':
    main()
