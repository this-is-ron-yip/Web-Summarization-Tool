from flask import Flask, jsonify, request
from flask_cors import CORS
from main import TextSummarizationAgent, WebSummarizationAgent

app = Flask(__name__)
CORS(app)

@app.route('/text', methods=['POST'])
def TextSummarization():
    text = request.form.get('content')
    response = TextSummarizationAgent(text)
    return response, 200


@app.route('/web', methods=['POST'])
def WebSummarization():
    url = request.form.get('content')
    response = WebSummarizationAgent(url)
    if response:
        return response, 200
    else:
        return '', 404