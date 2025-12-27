from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "100% LOCAL DevOps Project is LIVE 🚀"

app.run(host="0.0.0.0", port=5000)
