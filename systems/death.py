from engine import System


class DeathSystem(System):
    def __init__(self):
        super().__init__()

    def run(self):
        entities = self._engine.get_matching_entities(['creature'])
        for entity in entities:
            if self._engine.components['age'][entity] > 99 or self._engine.components['satiety'][entity] < 0.001:
                self._engine.fire_event((
                    'GUI_OUTPUT',
                    (
                        f"{self._engine.components['name'][entity]} died.",
                        'text'
                    )
                ))
                self._engine.remove_entity(entity)  # TODO: Change this to some sort of fired event for the engine to pick up on
