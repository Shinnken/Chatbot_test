# This is a web version of ChatBot.py, which uses Flask to create a web app.

# Importing Libraries
from flask import Flask, render_template, request
from BotDefinition import OpenAIBot

organization = 'org-yEvjHwO3In37mK5l8VfD8Utw'

# engine = "gpt-3.5-turbo"
# engine = "text-embedding-3-large"
engine = "gpt-4o-mini"
# Creating the Flask App
app = Flask(__name__)

# Importing Bot Defination
chatbot = OpenAIBot(engine)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    # Get Prompt from User
    prompt = request.form['prompt']

    # User can stop the chat by sending 'End Chat' as a Prompt
    if prompt.upper() == 'END CHAT':
        return 'END CHAT'

    # Generate and Print the Response from ChatBot
    response = chatbot.generate_response(prompt)
    return response

if __name__ == '__main__':
    app.run(debug=True)