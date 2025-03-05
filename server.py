from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({"message": "Hello, World from IBM Cloud Code Engine!"})

if __name__ == '__main__':
    # Bind to port 8080 for IBM Cloud Code Engine compatibility
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 8080)), debug=True)
