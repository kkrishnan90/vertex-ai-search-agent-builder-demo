import functools
from google.protobuf.json_format import MessageToDict
import coloredlogs
import logging
# A decorator function that takes in any number of argument

coloredlogs.install()
logger = logging.getLogger("Cymbal Search Application")

logger.setLevel(logging.DEBUG)

logger.info("Starting Cymbal Search Application")


def log_data(func):
    """
    Logs the input and output of a function.

    Args:
        func: The function to be decorated.

    Returns:
        The decorated function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
            logger.info("Showing environment variables")
            logger.info(response)
            return response
        except Exception as e:
            logging.exception(e)
            raise e
    return wrapper


def proto_to_dict(func):
    """
    Converts a protobuf message to a dictionary.

    Args:
        func: The function to be decorated.

    Returns:
        The decorated function.
    """
    @ functools.wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        result = MessageToDict(response._pb)
        logger.info(result)
        return result
    return wrapper
