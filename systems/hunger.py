from engine import System


class HungerSystem(System):
    def __init__(self):
        super().__init__()

    def run(self):
        entities = self._engine.get_matching_entities(['satiety'])
        for entity in entities:
            prev_satiety = self._engine.components['satiety'][entity]

            self._engine.components['satiety'][entity] -= 0.05
            if self._engine.components['satiety'][entity] < 0.0:
                self._engine.components['satiety'][entity] = 0.0

            if self._engine.components['satiety'][entity] <= 0.5 < prev_satiety:
                self._engine.fire_event((
                    'GUI_OUTPUT', (f"{self._engine.components['name'][entity]} is hungry.", 'text')
                ))
            if self._engine.components['satiety'][entity] <= 0.25 < prev_satiety:
                self._engine.fire_event((
                    'GUI_OUTPUT', (f"{self._engine.components['name'][entity]} is starving!", 'text')
                ))
