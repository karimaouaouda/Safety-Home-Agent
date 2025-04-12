from .base import BaseProcess


HOST = 'localhost'
PORT = 65432

def worker():
    # read shared memory content
    pass

class EagleEyesSystem(BaseProcess):
    def __init__(self, name: str, function: callable, args=None, kwargs=None):
        super().__init__(name, function, args, kwargs)
        # TODO implement this