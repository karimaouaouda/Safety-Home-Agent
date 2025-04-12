import abc
import json


class Notification(metaclass=abc.ABCMeta):
    def __init__(self, title, subtitle, message):
        self.title = title
        self.subtitle = subtitle
        self.message = message

    @abc.abstractmethod
    def notify(self):
        pass

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "subtitle": self.subtitle,
            "message": self.message,
        }


class WeirdPersonNotification(Notification):
    def notify(self):
        print("Weird Person Notification")


class MaterialExceptionNotification(Notification):
    def notify(self):
        print("Material Exception Notification")


