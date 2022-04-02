from engine import System


class GameTimeSystem(System):
    def __init__(self):
        super().__init__()
        self._seconds_since_epoch = 0.0
        self._seconds_per_tick = 1.0

    def run(self):
        self._seconds_since_epoch += self._seconds_per_tick

    def time_of_day(self):
        seconds_since_epoch = int(self._seconds_since_epoch)
        seconds = seconds_since_epoch % 60
        minutes_since_epoch = (seconds_since_epoch - seconds) // 60
        minutes = minutes_since_epoch % 60
        hours_since_epoch = (minutes_since_epoch - minutes) // 60
        hours = hours_since_epoch % 24
        return hours, minutes, seconds
