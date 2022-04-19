from flask import Blueprint, jsonify
from utils import get_posts_all, get_post_by_pk

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route("/posts/")
def get_posts_all():
    posts = get_posts_all()
    return jsonify(posts), {'Content-type': 'application/json; charset=utf-8'}


@api_blueprint.route("/posts/<int:post_id>")
def get_post_by_pk(pk):
    post = get_post_by_pk(pk)
    return jsonify(post), {'Content-type': 'application/json; charset=utf-8'}
