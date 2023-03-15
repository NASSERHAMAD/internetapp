from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "hello world!"
app.run( debug=True )


@app.route("/about")
def about():
    return render_template('abouthtml&css.html')