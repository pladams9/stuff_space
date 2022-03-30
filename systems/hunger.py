from engine import System


class HungerSystem(System):
    def __init__(self):
        super().__init__()

    def run(self):
        entities = self._engine.get_matching_entities(['satiety'])
        for entity in entities:
            self._engine.components['satiety'][entity] -= 0.05
            if self._engine.components['satiety'][entity] < 0.0:
                self._engine.components['satiety'][entity] = 0.0

