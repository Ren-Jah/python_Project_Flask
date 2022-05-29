import logging
from post_searcher import functions
from flask import Blueprint, render_template, request

from post_searcher.exceptions import DataSourceBrokenExceptions

main_blueprint = Blueprint('main_blueprint', __name__)

logger = logging.getLogger('basic')

@main_blueprint.route('/')
def main():
    return render_template('index.html')


@main_blueprint.route('/search', methods=["GET", "POST"])
def page_post_form():
    tag = request.args['s']

    logger.info(f'Searching by tag:{tag}')

    post_by_tag = functions.post_searcher(tag)
    return render_template('post_list.html', tag=tag, post_by_tag=post_by_tag)


@main_blueprint.errorhandler(DataSourceBrokenExceptions)
def data_source_broken(e):
    return render_template("data_source_broken.html")