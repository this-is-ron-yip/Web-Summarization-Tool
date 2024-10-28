from flask import Flask, jsonify, request
from main import TextSummarizationAgent


app = Flask(__name__)


@app.route('/text', methods=['GET'])
def TextSummarization():
    text = request.form.get('text')
    response = TextSummarizationAgent(text)
    return response