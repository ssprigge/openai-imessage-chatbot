import os
from flask import Flask, request
from sendblue import Sendblue
from dotenv import load_dotenv 
import json
from chatbot import ask

load_dotenv()

SENDBLUE_API_KEY = os.environ.get("SENDBLUE_API_KEY")
SENDBLUE_API_SECRET = os.environ.get("SENDBLUE_API_SECRET")
PORT = os.environ.get("PORT")

sendblue = Sendblue(SENDBLUE_API_KEY, SENDBLUE_API_SECRET)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET'

chat_logs = ['''The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.

Human: Hello, who are you?
AI: I am an AI created by OpenAI. How can I help you today?
'''
]

@app.route('/bot', methods=['POST'])
def bot():

    global chat_logs
    print(request.data)
    message_type = json.loads(request.data)['message_type']
    content = json.loads(request.data)['content']

    if message_type == 'message':

        from_number = json.loads(request.data)['from_number']
        answer, chat_logs = ask(content, chat_logs)
        response = sendblue.send_message(from_number, {'content': answer})

        return response

    elif message_type == 'group':

        group_id = json.loads(request.data)['group_id']
        participants = json.loads(request.data)['participants']
        answer, chat_logs = ask(content, chat_logs)
        response = sendblue.send_group_message({'numbers': participants, 'content': answer, 'group_id':group_id})
        
        return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)
