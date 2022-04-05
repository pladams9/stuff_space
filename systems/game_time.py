from engine import System


class GameTimeSystem(System):
    def __init__(self):
        super().__init__()
        self._seconds_per_tick = 60.0
        self._second = 0.0
        self._minute = self._hour = self._day = self._year = 0

    def run(self):
        new_minute = new_hour = new_day = new_year = False

        self._second += self._seconds_per_tick
        if self._second >= 60.0:
            self._second -= 60.0
            self._minute += 1
            new_minute = True
            if self._minute >= 60:
                self._minute -= 60
                self._hour += 1
                new_hour = True
                if self._hour >= 24:
                    self._hour -= 24
                    self._day += 1
                    new_day = True
                    if self._day >= 365:
                        self._day -= 365
                        self._year += 1
                        new_year = True

        time_summary = {
            'year': self._year,
            'day': self._day,
            'hour': self._hour,
            'minute': self._minute,
            'second': int(self._second)
        }
        self._engine.fire_event(('TIME_UPDATE', time_summary))
        if new_minute:
            self._engine.fire_event(('TIME_NEW_MINUTE', time_summary))
        if new_hour:
            self._engine.fire_event(('TIME_NEW_HOUR', time_summary))
        if new_day:
            self._engine.fire_event(('TIME_NEW_DAY', time_summary))
        if new_year:
            self._engine.fire_event(('TIME_NEW_YEAR', time_summary))
