from flask import Flask, render_template, redirect, url_for
import time
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/loading")
def loading():
    return render_template("loading.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/signup", methods=["POST"])
def signup():
    # 폼 데이터를 처리하는 코드
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080))))
