import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'thisisabadsessionprivatekey'
    TEMPLATES_AUTO_RELOAD = os.environ.get('TEMPLATES_AUTO_RELOAD') or True