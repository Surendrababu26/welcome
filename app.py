from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/data")
def get_data():
    # BACKEND LOGIC ONLY
    name = "surendra"
    return jsonify({"message": f"Hi {name}"})

if __name__ == "__main__":
    app.run(debug=True)
