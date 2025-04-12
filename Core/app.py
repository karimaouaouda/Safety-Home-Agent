from Core.server.classes import WebServer
from Core.server.notifications import MaterialExceptionNotification
from Core.utils.exceptions import MaterialException


class Application:
    def __init__(self):
        self.web_server:WebServer = WebServer('http://127.0.0.1:8000', 'api/v1')


    def start(self):
        # firstly when the application start we need to check the availability of the system
        try:
            self.check_materials()
        except MaterialException as e:
            feedback_message = {
                'traceback' : e.traceback,
                'message' : e.message,
            }
            self.web_server.send_notification(
                MaterialExceptionNotification('error n material', 'fix it now', feedback_message )
            )

        self.load_state()





    def check_materials(self):
        print("materials checked with 0 errors")

    def load_state(self):
        print("state loaded")
