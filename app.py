from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/run', methods=['POST'])
def run():
    return render_template("run.html")


if __name__ == '__main__':
    app.run(debug=True)
