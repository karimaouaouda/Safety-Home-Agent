from Core.server.classes import WebServer


class WebConfiguration:
    def __init__(self, webserver: WebServer):
        self.webserver = webserver


    def set(self, key, value):
        pass