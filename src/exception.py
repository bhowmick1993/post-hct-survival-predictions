import sys
import os
# Add the project root directory to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.logger import logging

def error_message_details(error, error_detail:sys):
    # this will return the error message and the line number
    _, _, exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(filename,
                                                                                                            exc_tb.tb_lineno,
                                                                                                            str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message) 

        self.error_message = error_message_details(error_message, error_detail)

    def __str__(self):
        return self.error_message
    

if __name__ == "__main__":
    try:
        a = 10/0
    except Exception as e:
        custom_exception = CustomException(e, sys)
        logging.error(custom_exception)
        raise custom_exception