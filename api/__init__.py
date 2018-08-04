import os

from flask import Flask

from api.models.req_helper import RequestHelper


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='something-SPECIAL-123-@#$',
        DATABASE=RequestHelper.req_db
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .views import request_view
    app.register_blueprint(request_view.req)

    return app
