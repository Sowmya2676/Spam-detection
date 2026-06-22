from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        message = request.form["message"]

        message_vector = vectorizer.transform([message])

        result = model.predict(message_vector)[0]

        prediction = "Spam ❌" if result == 1 else "Not Spam ✅"

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)