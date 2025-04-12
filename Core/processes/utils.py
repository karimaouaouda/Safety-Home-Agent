import socket
from threading import Thread


class WebSocket:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.worker:callable = None
        self.is_open = False
        self.thread = None

    def set_worker(self, worker: callable):
        self.worker = worker

    def start(self):
        if not self.worker:
            raise Exception('No worker defined')

        self.thread = Thread(target=self.worker)
        self.is_open = True
        self.thread.start()

    def stop(self):
        self.is_open = False
        self.thread.join()
        self.socket.close()
