from flask import Flask, render_template
from postdata import posts_data

app = Flask(__name__, template_folder='templates')


app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('home.html')
if __name__ == '__main__':
    app.run()
    
app = Flask(__name__)

@app.route('/')
def posts():
    return render_template('post_all.html', posts_data=posts_data)
if __name__ == '__main__':
    app.run(debug=True)    

app = Flask(__name__)

@app.route('/posts/<int:post_id>')
def post(post_id):
    post = None
    for p in posts_data:
        if p['id'] == post_id:
            post = p
            break
    return render_template('post-single.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)