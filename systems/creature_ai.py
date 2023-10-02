from engine import System
import random


class CreatureAI(System):
    def __init__(self):
        super().__init__()

    def run(self):
        entities = self._engine.get_matching_entities('creature')
        for entity in entities:
            if not self._ec(entity, 'creature')['alive']:  # TODO: Make 'alive' a separate component?
                continue

            # TODO: Add some sort of cooldown for actions? Actions should take up time.
            # TODO: Abstract the AI stuff more

            if random.random() < 0.1:
                if random.random() < 0.5:
                    exits = self._ec(entity, 'location')['exits']
                    if len(exits) > 0:
                        destination = exits[random.randint(0, len(exits) - 1)]
                        self._engine.fire_event((
                            'LOCATION_MOVE',
                            {
                                'entity': entity,
                                'destination': destination
                            }
                        ))
                else:
                    nearby = self._ec(entity, 'nearby_entities')
                    if len(nearby) > 0:
                        target = nearby[random.randint(0, len(nearby) - 1)]
                        self._engine.fire_event((
                            'CREATURE_INTERACTION',
                            {
                                'type': 'attack',
                                'primary': entity,
                                'target': target
                            }
                        ))
