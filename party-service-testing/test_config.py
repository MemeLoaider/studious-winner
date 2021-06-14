###test_config.py###
from os import path, environ
from dotenv import load_dotenv
from test_logic.party_service_implementation import PartyService
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from test_logic.models import PartyStuffWrapper
import pytest


# Specifying base dir and loading environment variables from .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


# Storing environment variables in these ones
ENVIRONMENT = environ.get('ENV')
PARTY_SERVICE_URL = environ.get('PARTY_SERVICE_URL')
GET_ALL_PARTIES_ENDPOINT = environ.get('GET_ALL_PARTIES_ENDPOINT')
GET_SINGLE_PARTY_ENDPOINT = environ.get('GET_SINGLE_PARTY_ENDPOINT')
CREATE_PARTY_ENDPOINT = environ.get('CREATE_PARTY_ENDPOINT')
UPDATE_HOST_ENDPOINT = environ.get('UPDATE_HOST_ENDPOINT')
DB_URL = environ.get('DB_URL')
DELETE_PARTY_ENDPOINT = environ.get('DELETE_PARTY_ENDPOINT')


# Creating fixtures for pytest below
@pytest.fixture(scope='session')
def party_service():
    return PartyService({
            'base_url': PARTY_SERVICE_URL,
            'get_all_parties_endpoint': GET_ALL_PARTIES_ENDPOINT,
            'create_party_endpoint': CREATE_PARTY_ENDPOINT,
            'update_party_host_endpoint': UPDATE_HOST_ENDPOINT,
            'delete_party_by_id_endpoint': DELETE_PARTY_ENDPOINT,
            'get_single_party_by_id': GET_SINGLE_PARTY_ENDPOINT
        })


@pytest.fixture(scope='session')
def db_session():
    engine = create_engine(DB_URL, echo=False) 
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    print('closing db session...')
    session.close()


@pytest.fixture(scope='session')
def db_wrapper(db_session) -> PartyStuffWrapper:
    return PartyStuffWrapper(db_session)

