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
    SQLALCHEMY_DATABASE_URI = 'postgresql://dung:@localhost:5432/mydata'
    TEMPLATES_AUTO_RELOAD = True

class ProductionConfig(Config):
    """
    Envirement production
    """

    JWT_SECRET_KEY = 'super-secret' # Change this!
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours = 1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days = 30)
    SQLALCHEMY_DATABASE_URI = 'postgresql://dungAws:@52.68.119.104:5433/myawsdata'
    TEMPLATES_AUTO_RELOAD = True

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
