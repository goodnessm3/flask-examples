from flask import Flask
import os
from subprocess import Popen

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='rutbaga',
        PERMANENT_SESSION_LIFETIME=157000000,
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import start
    app.register_blueprint(start.bp)

    return app


_ = Popen(r"websocketd/websocketd --port=8080 tail -f alog.txt", shell=True)
# monitor the gunicorn log and have websocketd read it with tail and send it to the browser page
app = create_app()

