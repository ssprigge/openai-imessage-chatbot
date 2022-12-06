import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.environ.get('OPENAI_KEY')
completion = openai.Completion()

def ask(question, chat_log):

    chat_log.append(f'Human: {question}\nAI:')
    prompt = ''.join(chat_log) 
    print(prompt)
    response = completion.create(
        prompt=prompt, model="text-davinci-003", temperature=0.9, top_p=1,
        frequency_penalty=0, presence_penalty=0.6, best_of=1,
        max_tokens=150)
    answer = response.choices[0].text.strip()
    chat_log.append(f' {answer}\n')

    return answer, chat_log
