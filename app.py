from flask import Flask, render_template, request, jsonify
import json
from tests import run_tests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-data', methods=['GET'])
def get_data():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    return jsonify(data)

@app.route('/run-tests', methods=['POST'])
def run_tests_route():
    data = request.json
    
    with open('data.json', 'w') as f:
        json.dump(data, f)

    run_tests(data)
    
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

