import traceback

class MaterialException(BaseException):
    def __init__(self, message):
        self.message = message
        self.traceback = traceback.format_exc()