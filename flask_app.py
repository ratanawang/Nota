from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "main":
    app.run(debug=True)
