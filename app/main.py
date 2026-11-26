from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Aprender Docker", "done": True},
    {"id": 2, "title": "Terminar proyecto final", "done": False},
]


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
