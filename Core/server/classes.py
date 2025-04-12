from Core.server.apis import NotificationApi
from Core.server.helpers import build_url
from Core.server.notifications import Notification
from Core.server.apis import NotificationApi
import requests


class WebServer:
    def __init__(self, base_url, api_uri_prefix='/api/v1'):
        self.base_url = base_url
        self.api_uri = api_uri_prefix
        self.notification_api:NotificationApi|None = None
        self.setup()

    def setup(self):
        self.notification_api = NotificationApi(api_base_url=build_url(self.base_url, self.api_uri), api_prefix='notifications')

    def send_notification(self, notification: Notification):
        data = notification.to_dict()
        response = self.notification_api.post(data)
        return response



    def configuration(self):
        if self.configuration:
            return self.configuration
        else:
            self.configuration = WebConfiguration(self)
            return self.configuration
