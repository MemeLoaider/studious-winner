###Flask Configuration"""
from os import path, environ
from dotenv import load_dotenv 


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Base configuration for Flask"""


class LocalConfig(Config):
    """Configuration for running Flask locally"""
    FLASK_ENV = environ.get('FLASK_ENV')
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


