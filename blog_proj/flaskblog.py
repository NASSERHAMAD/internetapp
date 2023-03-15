from flask import Flask
app = Flask(__name__)
app.secret_key = 'fdb1eefad885bf835e1dea884244221'

@app.route("/")
def hello():
    return "hello world!"