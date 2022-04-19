from flask import Flask, send_from_directory, render_template, request

from utils import *
from api.api import api_blueprint
app = Flask(__name__)
app.register_blueprint(api_blueprint, url_prefix='/api')


@app.route('/')
def main():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)


@app.route("/img/<path:path>")
def static_dir(path):
    return send_from_directory("static/img", path)


@app.route('/post/<int:postid>')
def profile(postid):
    comments = get_comments_by_post_id(postid)
    post = get_post_by_pk(postid)
    return render_template('post.html', comments=comments, post=post)


@app.route('/search/')
def search_post():
    search_word = request.args.get('s')
    querys = search_for_posts(search_word)
    return render_template('search.html', querys=querys)


@app.route('/users/<username>')
def users(username):
    names = get_posts_by_user(username)
    return render_template('user-feed.html', names=names)


if __name__ == "__main__":
    app.run()
