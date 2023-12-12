from datetime import datetime


class DateMessage:
    def __init__(self, message):
        self.date = datetime.now()
        self.message = message
