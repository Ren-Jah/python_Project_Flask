import logging
from post_searcher import functions
from flask import Blueprint, render_template, request

from post_searcher.exceptions import PictureNotUploadError

loader_blueprint = Blueprint('loader_blueprint', __name__)

logger = logging.getLogger('basic')

@loader_blueprint.route('/post_upload')
def post_form():
    return render_template('post_form.html')


@loader_blueprint.route('/post_upload', methods=["POST"])
def post_loader():
    picture = request.files.get("picture")
    filename = picture.filename
    content = request.form.get("content")
    if functions.is_filename_allowed(filename):
        try:
            picture.save(f"./uploads/images/{filename}")
        except:
            logger.error(f"Can't load:{filename}")
            raise PictureNotUploadError(f"./uploads/images/{filename}")


        picture_url = f"./uploads/images/{filename}"
        functions.post_to_json(picture_url, content)
        return render_template('post_uploaded.html', picture=picture_url, content=content)
    else:
        extension = filename.split(".")[-1]
        return render_template('extension.html', extension=extension)


@loader_blueprint.errorhandler(PictureNotUploadError)
def picture_not_upload(e):
    return render_template('picture_not_upload.html')
