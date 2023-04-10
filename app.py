from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title='Home')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
