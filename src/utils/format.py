from dateutil import parser
import datetime


class Date(object):
    @property
    def now(self):
        return self.timer(datetime.datetime.now())

    @staticmethod
    def timer(date: str):
        c_time = parser.parse(date)
        return c_time.strftime("%Y-%m-%d %H:%M:%S")
