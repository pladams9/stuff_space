from engine import System


class AgingSystem(System):
    def __init__(self):
        super().__init__()

    def run(self):
        entities = self._engine.get_matching_entities(['age'])
        for entity in entities:
            self._engine.components['age'][entity] += 1
