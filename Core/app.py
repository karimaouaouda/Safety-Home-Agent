from Core.processes.base import BaseProcess
from Core.server.classes import WebServer
from Core.server.notifications import MaterialExceptionNotification
from Core.utils.exceptions import MaterialException
from Core.processes.eagle_eyes import EagleEyesSystem


class Application:
    def __init__(self):
        # start the global server ( hosted )
        self.web_server:WebServer = WebServer('http://127.0.0.1:8000', 'api/v1')
        self.local_server:WebServer = WebServer('http://127.0.0.1:4000', '')
        self.processes:list[BaseProcess] = []

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


        # let's load the state  from the shared memory
        self.load_state()


        self.run_processes()


    def run_processes(self):
        cameras_process = EagleEyesSystem("eagle")
        cameras_process.start()








    def check_materials(self):
        print("materials checked with 0 errors")

    def load_state(self):
        print("state loaded")
