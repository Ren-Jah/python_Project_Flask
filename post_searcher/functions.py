import json

from post_searcher.exceptions import DataSourceBrokenExceptions

POST_PATH = "posts.json"

from pprint import pprint as pp

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def load_posts_from_json(path=POST_PATH):
    """возвращает список всех постов"""
    try:
        with open(path, 'r', encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):

        raise DataSourceBrokenExceptions("Файл с данными поврежден")

    return data


def post_searcher(tag):
    """Выдает посты по слову"""
    posts = load_posts_from_json()
    post_by_tag = []
    for post in posts:
        if tag.lower() in post["content"]:
            post_by_tag.append(post)
            continue
    return post_by_tag


def post_to_json(picture, content, path=POST_PATH):
    entry = {"pic": picture, "content": content}

    with open(path, 'r', encoding="utf-8") as file:
        data = json.load(file)
    data.append(entry)
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def is_filename_allowed(filename):
    extension = filename.split(".")[-1]
    if extension.lower() in ALLOWED_EXTENSIONS:
        return True
    return False



