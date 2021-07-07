from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify(state="up")


if __name__ == "__main__":
    app.run("0.0.0.0", 8080)
