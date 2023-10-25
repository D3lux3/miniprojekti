import random
from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

file_paths = ["wrangler/wrangled_data_part1.csv", "wrangler/wrangled_data_part2.csv"]
df = pd.concat([pd.read_csv(path) for path in file_paths], ignore_index=True)

app = Flask(__name__)
CORS(app, origins="http://localhost:5173", supports_credentials=True)


@app.route("/", methods=["GET"])
def get_message():
    return jsonify(message="Hello")

@app.route("/randrank", methods=["GET"])
def get_random_rank():
    return jsonify(rank=round(random.uniform(0.00, 100.00), 2))

@app.route("/", methods=["POST"])
def update_message():
    data = request.json
    word = data.get("input_word", "")
    print(word)
    return jsonify(message=f"Cool {word} video")

@app.route("/data", methods=["GET"])
def get_sample():
    sample = df.head().to_json(orient="records")
    return jsonify(data=sample)


if __name__ == "__main__":
    app.run(debug=True)