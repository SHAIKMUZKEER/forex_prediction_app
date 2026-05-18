from flask import Flask, render_template, request
import pickle
import numpy as np


app = Flask(__name__)


model = pickle.load(open("model.pkl", "rb"))


scaler = pickle.load(open("scaler.pkl", "rb"))



@app.route("/")
def home():

    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Get input values from HTML form
        bid_open = float(request.form["bid_open"])
        bid_high = float(request.form["bid_high"])
        bid_low = float(request.form["bid_low"])

        # Convert input into numpy array
        features = np.array([[bid_open, bid_high, bid_low]])

        # Scale features
        scaled_features = scaler.transform(features)

        # Predict BID CLOSE price
        prediction = model.predict(scaled_features)

        # Get prediction value
        predicted_bid_close = round(prediction[0], 5)

        # Return result to webpage
        return render_template(
            "index.html",
            prediction_text=f"Predicted BID CLOSE Price: {predicted_bid_close}"
        )

    except Exception as e:

        return render_template(
            "index.html",
            prediction_text=f"Error: {str(e)}"
        )



if __name__ == "__main__":

    app.run(debug=True)