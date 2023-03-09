import sys

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    line_number=exc_tb.tb_lineno
    message=str(error)

    error_message="Error occured while executing python script name [{0}] at line number [{1}] error message[{2}]".format(
        file_name,line_number,message
    )

    return error_message


class CustomExcpetion(Exception):
    def __init__(self, error_message,error_detail) -> None:
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail)
    
    def __str__(self) -> str:
        return self.error_message