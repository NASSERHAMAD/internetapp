from flask import Flask, render_template
from postsdata import posts

app = Flask(__name__)

@app.route('/posts')
def posts_page():
    return render_template('post-all.html', posts=posts)

if __name__ == '__main__':
    app.run()

