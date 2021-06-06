###test_config.py###
from os import path, environ
from dotenv import load_dotenv


# Specifying base dir and loading environment variables from .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


ENVIRONMENT = environ.get('ENV')
PARTY_SERVICE_URL = environ.get('PARTY_SERVICE_URL')
GET_ALL_PARTIES_ENDPOINT = environ.get('GET_ALL_PARTIES_ENDPOINT')
CREATE_PARTY_ENDPOINT = environ.get('CREATE_PARTY_ENDPOINT')

