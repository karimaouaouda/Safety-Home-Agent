from .base import BaseProcess


HOST = 'localhost'
PORT = 65432

def worker():
    # read shared memory content
    pass

class EagleEyesSystem(BaseProcess):
    def __init__(self, name: str):
        super().__init__(name)
        # TODO implement this