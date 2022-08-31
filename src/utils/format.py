from dateutil import parser
import datetime


class Date(object):
    @property
    def now(self):
        return lambda: self.timer(datetime.datetime.now())

    @staticmethod
    def timer(date: str):
        c_time = parser.parse(str(date))
        return c_time.strftime("%Y-%m-%d %H:%M:%S")
