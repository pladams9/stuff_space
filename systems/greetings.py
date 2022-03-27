from engine import System
import time


class GreetingsSystem(System):
    def __init__(self):
        super().__init__()
        self._seconds_between_greetings = 1
        self._time_of_last_greeting = time.time() - self._seconds_between_greetings

    def run(self):
        if time.time() - self._time_of_last_greeting > self._seconds_between_greetings:
            self._time_of_last_greeting = time.time()
            entities = self._engine.get_matching_entities(['name', 'greeting'])
            for entity in entities:
                self._engine.fire_event((
                    'GUI_OUTPUT',
                    f"[{time.strftime('%H:%M:%S')}] {self._engine.components['name'][entity]} says \"{self._engine.components['greeting'][entity]}\""
                ))
