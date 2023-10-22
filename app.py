from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/birds', methods=['GET'])
def get_birds():
    with open('basic_birds.json', 'r', encoding='utf-8') as file:
        birds_data = json.load(file)
    return jsonify(birds_data)


@app.route('/birds', methods=['POST'])
def add_bird():
    new_bird = request.get_json()

    with open('basic_birds.json', 'r', encoding='utf-8') as file:
        birds_data = json.load(file)
    birds_data.append(new_bird)

    with open('basic_birds.json', 'w', encoding='utf-8') as file:
        json.dump(birds_data, file, ensure_ascii=False, indent=4)

    return jsonify(new_bird), 201


if __name__ == '__main__':
    app.run()
