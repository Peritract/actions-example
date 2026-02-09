"""Functions to manipulate text in specifically stupid ways."""

from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    return "I am working!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
