from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route("/predict", methods=["GET"])
def predict():
    # Dummy AI prediction logic
    prediction = {
        "Size": random.choice(["Big", "Small"]),
        "Colour": random.choice(["Red", "Green", "Violet"]),
        "Number": random.randint(0, 9),
        "Confidence": f"{random.randint(70, 95)}%"
    }
    return jsonify(prediction)

if __name__ == "__main__":
    app.run(debug=True)
