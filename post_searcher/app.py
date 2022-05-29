import logging
from flask import Flask, render_template, send_from_directory
from main.views import main_blueprint
from loader.views import loader_blueprint
import loggers

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

app.register_blueprint(main_blueprint)

app.register_blueprint(loader_blueprint)

loggers.create_logger()

logger = logging.getLogger('basic')


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


@app.errorhandler(413)
def page_not_found(e):
    return render_template('page_not_found.html')


logger.info("Приложение запускается")

if __name__ == '__main__':
    app.run(debug=True)
