###Flask Configuration"""
from os import path, environ


basedir = path.abspath(path.dirname(__file__))


class Config:
    """Base configuration for Flask"""


class LocalConfig(Config):
    """Configuration for running Flask locally"""
    FLASK_ENV = 'local'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1234@localhost:3307/mysql"#environ.get('LOCAL_DB_MYSQL')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
