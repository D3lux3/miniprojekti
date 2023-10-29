import random
from flask import Flask, jsonify, request
from flask_cors import CORS
import csv
import json
import re
import zipfile

from nltk.stem.porter import *

with open("eda/word_rank.csv", mode="r") as file:
    r = csv.reader(file)
    word_rank = {row[0]: float(row[1]) for row in r}

with zipfile.ZipFile("title-gen/word_gen_computed.zip", 'r') as zip_ref:
    with zip_ref.open(zip_ref.namelist()[0], "r") as file:
        predict_data = json.load(file)

def rank_title(input):
    print(input)
    input = re.sub(r"[^\w\s]", "", input.lower()) # remove punctuations and change to lower
    stemmed_words = [PorterStemmer().stem(word) for word in str(input).split()] # stemming
    return round(sum(word_rank.get(word, 0) for word in stemmed_words), 2)

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

@app.route("/generate", methods=["POST"])
def get_next_word():
    if request.is_json:
        data = request.get_json()
        if not ("previous" in data and "chaos" in data):
            return jsonify("Error: request missing attributes")
        previous = data["previous"]
        chaos = data["chaos"]

        # the input (previous) should be two words
        # if this combination is not found, we try just the previous one word    
        if not previous in predict_data:
            split = previous.split(" ")
            if len(split) > 1:
                previous = split[len(split) - 1]
        if previous in predict_data:
            all_next = predict_data[previous]
            index = random.randint(0, min(len(all_next), chaos))
            return jsonify(word=all_next[index])
        return jsonify("{}")
    return jsonify("{Error: badly formatted request}")

if __name__ == "__main__":
    app.run(debug=True)