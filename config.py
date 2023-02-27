# config.py
import os
from datetime import timedelta

class Config(object):
    """
    Envirement common
    """
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'

class DevelopmentConfig(Config):
    """
    Envirement development
    """

    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_ECHO = True

    JWT_SECRET_KEY = 'super-secret' # Change this!
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours = 1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days = 30)
    SQLALCHEMY_DATABASE_URI = 'postgresql://dung:@localhost/mydata'
    TEMPLATES_AUTO_RELOAD = True

    # Connect to databases
    DB_NAME = 'mydata'
    HOST_NAME = 'localhost'
    USERNAME = 'dung'
    PASSWORD = ''

class ProductionConfig(Config):
    """
    Envirement production
    """

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
