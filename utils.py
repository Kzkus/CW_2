import json


def get_posts_all():
    with open("data/data.json", "r", encoding="utf-8") as file:
        posts = json.load(file)
    # возвращает посты
    return posts


def get_posts_by_user(user_name):
    return [user for user in get_posts_all() if user_name.lower() in user['poster_name']]

    # возвращает посты определенного пользователя


def get_comments_by_post_id(post_id):
    with open("data/comments.json", "r", encoding="utf-8") as file:
        comments = json.load(file)
    comments_by_post = []
    for comment in comments:
        if post_id == comment["post_id"]:
            comments_by_post.append(comment)
    return comments_by_post


# возвращает комментарии определенного поста

def search_for_posts(query):
    posts = []
    for post in get_posts_all():
        querys = post['content']
        if query.lower() in querys.lower():
            posts.append(post)
    return posts[:10]
    # возвращает список постов по ключевому слову


def get_post_by_pk(pk: int):
    for post in get_posts_all():
        if pk == post["pk"]:
            return post
    return "Такого поста нет"
    # возвращает один пост по его идентификатору
