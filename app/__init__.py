from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.flatpages import FlatPages
from config import config

bootstrap = Bootstrap()
flatpages = FlatPages()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    flatpages.init_app(app)

    # from . import views

    return app

app = create_app("default")

from . import views
