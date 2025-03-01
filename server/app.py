from flask import Flask, jsonify, request
from flask_cors import CORS  

app = Flask(__name__)
CORS(app) 


@app.route('/predict', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello from backend sounds-like!"})


@app.route('/predict', methods=['POST'])
def post_data():
    data = request.json
    return jsonify({"received": data})

if __name__ == '__main__':
    app.run(debug=True)