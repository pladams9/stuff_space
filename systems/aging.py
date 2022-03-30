from engine import System


class AgingSystem(System):
    def __init__(self):
        super().__init__()

    def run(self):
        entities = self._engine.get_matching_entities(['age'])
        for entity in entities:
            self._engine.components['age'][entity] += 1
            self._engine.fire_event((
                'GUI_OUTPUT',
                (f"{self._engine.components['name'][entity]} just turned {self._engine.components['age'][entity]}.", 'text')
            ))
