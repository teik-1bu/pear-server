# -*- coding: utf-8 -*-

import os


class BaseConfig(object):
    # Get app root path
    # ../../configs/configs.py
    _basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    PROJECT = "ApiPlayFPT"
    DEBUG = True
    TESTING = False


class DevConfig(BaseConfig):
    DEBUG = True


class TestConfig(BaseConfig):
    TESTING = True
