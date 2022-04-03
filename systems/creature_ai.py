from engine import System
import random


class CreatureAI(System):
    def __init__(self):
        super().__init__()

    def run(self):
        entities = self._engine.get_matching_entities('creature')
        for entity in entities:
            if not self._engine.components['creature'][entity]['alive']:
                continue
            nearby = self._engine.components['nearby_entities'][entity]
            target = nearby[random.randint(0, len(nearby) - 1)]

            r = random.random()
            if r < 0.1:
                # Dinosaur tries to attack
                self._engine.fire_event((
                    'CREATURE_INTERACTION',
                    {
                        'type': 'attack',
                        'primary': entity,
                        'target': target
                    }
                ))
