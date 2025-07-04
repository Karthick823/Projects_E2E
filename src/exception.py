import sys

def error_message_detail(error, error_detail:sys): # type: ignore
    _,_, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename # type: ignore
    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(  # noqa: F841
        file_name, exc_tb.tb_lineno,str(error)) # type: ignorereturn error_message # type: ignore
        
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys) -> None: # type: ignore
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    def __str__(self) -> str:
        return self.error_message # type: ignore