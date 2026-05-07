from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>DevOps Containerisation Evidence</h1>
    <p>This Python Flask application is running inside a Docker container.</p>
    <p>This supports my PDP goal of developing foundational DevOps skills.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
