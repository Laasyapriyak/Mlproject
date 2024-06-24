import sys
import logging
#any exception is being cotrolled then this sys
#this sys library will have that information
def error_message_details(error,error_detail:sys):
    _,_,exe_tb=error_detail.exc_info()
    file_name=exe_tb.tb_frame.f_code.co_filename
    error_mesage="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format()
    file_name,exe_tb.tb_lineno,str(error)
    return error_mesage

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super.__init__(error_message)
        self.error_message=error_message_details(error_message,error_detail=error_detail)
    def __str__(self):
        return self.error_message






