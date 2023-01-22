from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response
import nltkmodules
app = Flask(__name__)
CORS(app)

@app.get("/")
def index_get():
    return "Hello, Welcome to Minichatbot!"

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # Checks if text is valid
    reponse = get_response(text)
    message = {"answer" : reponse}
    return jsonify(message)

# if __name__ == "__main__":
#     app.run(debug=True)