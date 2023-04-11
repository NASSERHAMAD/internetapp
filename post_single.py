from flask import Flask, render_template
from postsdata import posts

app = Flask(__name__)

# Route for single post page
@app.route('/posts/<int:post_id>')
def post_single(post_id):
    # Find the post with the given post_id
    post = None
    for p in posts:
        if p['id'] == post_id:
            post = p
            break

    if post is not None:
        return render_template('post-single.html', post=post)
    else:
        return "Post not found", 404

if __name__ == '__main__':
    app.run()
