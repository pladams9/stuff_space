from engine import System
import time


class AgingSystem(System):
    def __init__(self):
        super().__init__()
        self._seconds_to_year = 5
        self._time_of_last_tick = time.time()

    def run(self):
        if time.time() - self._time_of_last_tick > self._seconds_to_year:
            self._time_of_last_tick = time.time()
            entities = self._engine.get_matching_entities(['age'])
            for entity in entities:
                self._engine.components['age'][entity] += 1
