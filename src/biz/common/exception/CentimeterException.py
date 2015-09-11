__author__ = 'chenjinlong'


class CentimeterException(Exception):
    def __init__(self, msg, *args, **kwargs):
        self.msg = msg

class ErrorTypeException(CentimeterException):
    def __init__(self, msg, *args, **kwargs):
        super(ErrorTypeException,self).__init__(msg,*args,**kwargs)
