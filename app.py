from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Welcome to my Flask app!"

@app.route("/data")
def get_data():
    name = "surendra"
    return jsonify({"message": f"Hi {name}"})

if __name__ == "__main__":
    app.run(debug=True)
