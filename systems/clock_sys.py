from engine import System


class ClockSystem(System):
    LISTENERS = ['TIME_UPDATE', 'TIME_NEW_DAY', 'GUI_INPUT']

    def __init__(self):
        super().__init__()
        self._time = {
            'year': 0,
            'day': 0,
            'hour': 0,
            'minute': 0,
            'second': 0
        }

    def run(self):
        while not self.events.empty():
            e = self.events.get()
            if e[0] == 'TIME_UPDATE':
                self._time = e[1]
            if e[0] == 'TIME_NEW_DAY' or (e[0] == 'GUI_INPUT' and e[1] == 'clock'):
                self._engine.fire_event((
                    'GUI_OUTPUT',
                    (
                        f"{self._time['year']:04}-{self._time['day']:03} {self._time['hour']:02}:{self._time['minute']:02}:{self._time['second']:02}",
                        'text'
                    )
                ))
