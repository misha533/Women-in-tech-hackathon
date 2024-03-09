from flask import Flask, render_template, request, jsonify, Response, send_file
import openai

app = Flask(__name__)

openai.api_key = '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'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bot')
def bot():
    return render_template('bot.html')


messages = [
{"role": "system", "content": "Hello! I am a chatbot. Ask me anything."},
]

if __name__ == '__main__':
    app.run(debug=True)