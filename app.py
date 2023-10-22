from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route('/birds', methods=['GET'])
def get_birds():
    with open('basic_birds.json', 'r', encoding='utf-8') as file:
        birds_data = json.load(file)
    return jsonify(birds_data)


if __name__ == '__main__':
    app.run()
