# openai-imessage-chatbot

An iMessage ChatBot using OpenAI's GPT-3, sendblue, and Python.

(Inspired by Miguel Grinberg's [SMS ChatBot](https://www.twilio.com/blog/openai-gpt-3-chatbot-python-twilio-sms))

![image](https://user-images.githubusercontent.com/80603352/205788265-0869061b-7a73-40e9-96ee-74a9c2272d01.png)

## Mac OS Installation
**In desired directory:** 

Clone repository
```
$ git clone https://github.com/ssprigge/openai-imessage-chatbot
```
Create Python Virtual Environment
```
$ python3 -m venv venv
```
Activate Virtual Environment
```
$ source venv/bin/activate
```
Install requisite Python Modules
```
(venv) $ pip install openai sendblue flask python-dotenv pyngrok
```
## Configuration
Requires an [OpenAI](https://openai.com/) account and a [sendblue](https://sendblue.co) account.

A (free) [ngrok](https://ngrok.com) account is recommended.

If you have set up an [ngrok](https://ngrok.com) account, authenticate it by executing
```
(venv) $ ngrok config add-authtoken your-authentication-token
```
Where `your-authentication-token` is your ngrok authentication token, found at https://dashboard.ngrok.com/get-started/your-authtoken

In *.env* file, define `OPENAI_KEY`, `SENDBLUE_API_KEY`, and `SENDBLUE_API_SECRET`, using the keys from your OpenAI and sendblue accounts.

(Found at https://beta.openai.com/account/api-keys and https://sendblue.co/dashboard/api respectively.)
```
OPENAI_KEY=your-openai-key
SENDBLUE_API_KEY=your-senblue-api-key
SENDBLUE_API_SECRET=your-sendblue-api-secret
```

Also, in *.env* file, define `PORT` as desired **unused** port e.g. 5000 or 9000.

```
PORT=your-unused-port
```

## Running the App Locally
Open two new terminal windows. 

In both terminals, navigate to the directory containing the cloned project.

In both terminals, activate the Python Virtual Environment
```
$ source venv/bin/activate
```

In one terminal, run
```
(venv) $ ngrok http PORT
```
Where the word PORT is replaced by the number of the unused port, as defined in the *.env* file.

You should see a window similar to

![image](https://user-images.githubusercontent.com/80603352/205755819-d91d1624-8536-4790-8abd-877a6a3c698e.png)

From this window, copy the Forwarding URL beginning with *https:* into the Webhooks Receive Textbox, found in the sendblue APIDashboard tab (https://sendblue.co/dashboard/api).

Append */bot* to the end of the URL in the box, then press the blue Save button.

![image](https://user-images.githubusercontent.com/80603352/205761682-6ddd8dba-d0c3-4afe-b721-6c58481bd621.png)

(Note: If you are using a free ngrok account, the Forwarding URL will change every time you run `(venv) $ ngrok http PORT`)

In the terminal **not** running `ngrok` execute 
```
(venv) $ python app.py
```

Finally, to interact with the ChatBot, simply send an iMessage to the phone number provided to you in your sendblue account.

## Deactivating App
To Deactivate the App, press <kbd>control</kbd>+<kbd>C</kbd> while in the terminal running `app.py`.

To exit Python Virtual Environment, execute
```
(venv) $ deactivate
```

## Limitations
- Once `app.py` is run, the same chat will persist across different iMessage instances, until `app.py` is terminated.

- Due to GPT-3's input token limit and the manner in which the app prompts GPT-3, a sufficiently long chat will exceed the token limit and the bot will stop responding.

- App works best if users wait for a reponse before sending another message
