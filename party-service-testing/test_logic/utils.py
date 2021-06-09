import logging
import functools


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
        
