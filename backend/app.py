from flask import Flask, jsonify, request
from main import TextSummarizationAgent, WebSummarizationAgent


app = Flask(__name__)


@app.route('/text', methods=['GET'])
def TextSummarization():
    text = request.form.get('text')
    response = TextSummarizationAgent(text)
    return response, 200


@app.route('/web', methods=['GET'])
def WebSummarization():
    url = request.form.get('url')
    response = WebSummarizationAgent(url)
    if response:
        return response, 200
    else:
        return '', 404