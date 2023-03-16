from flask import Flask , render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return "hello world!"
app.run( debug=True )


@app.route("/about")
def about():
    return render_template('abouthtmlcss.html')


