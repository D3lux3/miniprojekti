import random
from flask import Flask, jsonify, request
from flask_cors import CORS
import csv
import re
from nltk.stem.porter import *

with open("eda/word_rank.csv", mode="r") as file:
    r = csv.reader(file)
    word_rank = {row[0]: float(row[1]) for row in r}

def rank_title(input):
    print(input)
    input = re.sub(r"[^\w\s]", "", input.lower()) # remove punctuations and change to lower
    stemmed_words = [PorterStemmer().stem(word) for word in str(input).split()] # stemming
    return sum(word_rank.get(word, 0) for word in stemmed_words)

app = Flask(__name__)
CORS(app, origins="http://localhost:5173", supports_credentials=True)


@app.route("/", methods=["GET"])
def get_message():
    return jsonify(message="Hello")

@app.route("/rank", methods=["POST"])
def rank_input_title():
    data = request.json
    title = data.get("text", "")
    return jsonify(rank=rank_title(title))


if __name__ == "__main__":
    app.run(debug=True)