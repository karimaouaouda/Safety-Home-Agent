from multiprocessing import Process, Queue

class BaseProcess:
    def __init__(self, name:str, function:callable, args=None, kwargs=None):
        self.name = name
        self.function = function
        self.args = args
        self.kwargs = kwargs

        self.process:Process|None = None

        self.setup()

    def setup(self):
        try:
            self.create_process()
        except ChildProcessError as e:
            print("failed to create process")

    def create_process(self):
        self.process = Process(target=self.function, args=(self.args,), kwargs=self.kwargs)

    def get_pid(self):
        return self.process.pid

    def start(self):
        self.process.start()

    def stop(self):
        self.process.terminate()

    def join(self):
        self.process.join()
