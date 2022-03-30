from engine import System
import random


class DeathSystem(System):
    def __init__(self):
        super().__init__()

    def run(self):
        entities = self._engine.get_matching_entities(['creature'])
        for entity in entities:
            death_chance = 1.0 - pow((1.0 / ((self._engine.components['age'][entity] / 100.0) + 1.0)), (1.0 / 365.0))
            if random.random() < death_chance:
                self._engine.fire_event((
                    'GUI_OUTPUT',
                    (
                        f"{self._engine.components['name'][entity]} died.",
                        'text'
                    )
                ))
                self._engine.remove_entity(entity)  # TODO: Change this to some sort of fired event for the engine to pick up on
