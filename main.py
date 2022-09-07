from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    test_var = 444
    return render_template("index.html", content=test_var)


if __name__ == "__main__":
    app.run()
