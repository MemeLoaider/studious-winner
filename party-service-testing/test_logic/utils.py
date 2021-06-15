import logging
import functools
import random


# Creating logger with stream handler
LOGGER = logging.Logger(__name__)
LOGGER.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter("%(asctime)s:%(message)s"))
LOGGER.addHandler(stream_handler)


def log_request_and_response(request_method, endpoint):
    def log_decorator(func):
        @functools.wraps(func)
        def wrapper_log_request_and_response(*args, **kwargs):
            LOGGER.info(f"SENDING {request_method}-REQUEST TO {args[0].base_url}{args[0].dictionary[endpoint]}")
            result = func(*args, **kwargs)
            LOGGER.info(f"RESPONSE DATA: {str(result)}")
            return result
        return wrapper_log_request_and_response
    return log_decorator
        

class Generator:
    
    def __init__(self, db_wrapper):
        self.db_wrapper = db_wrapper


    def get_incorrect_party_id(self):
        """Methos is used to return incorrect_party_id
        Uses db_session in order to check existing party_ids in order to return incorrect one"""
        # Getting all valid party_ids in order to set invalid one
        list_of_party_ids = []
        for party in self.db_wrapper.get_all_parties_from_db():
            list_of_party_ids.append(party.party_id)

        incorrect_party_id = None
        while True:
            incorrect_party_id = random.randint(list_of_party_ids[-1], 1000)
            if incorrect_party_id not in list_of_party_ids:
                return incorrect_party_id


