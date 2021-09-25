import time
class alarm:
    def __init__(self, time_ = time.time(), alarm_ = "Alarm"):
        self.time = time_
        self.name = alarm_
    def check(self):
        return self.time >= time.time()
