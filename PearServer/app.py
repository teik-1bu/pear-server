# -*- coding: utf-8 -*-

from flask import Flask
from flask_cors import CORS

from .configs import DevConfig
from .restApi.node import rest_node

# For import *
__all__ = ['create_app']

DEFAULT_BLUEPRINTS = (
    rest_node,
)


def create_app(config=None, app_name=None, blueprints=None):
    """Create a Flask app."""

    if app_name is None:
        app_name = DevConfig.PROJECT
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS

    app = Flask(app_name)
    CORS(app, expose_header=['*'])
    configure_app(app, config)
    configure_blueprints(app, blueprints)

    return app


def configure_app(app, config):
    """Configure app from object, parameter and env."""

    app.config.from_object(DevConfig)
    if config is not None:
        app.config.from_object(config)
    # Override setting by env var without touching codes.
    app.config.from_envvar('%s_APP_CONFIG' % DevConfig.PROJECT.upper(), silent=True)


def configure_blueprints(app, blueprints):
    """Configure blueprints in views."""

    for blueprint in blueprints:
        app.register_blueprint(blueprint)
