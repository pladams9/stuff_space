from engine import System


class LocationSystem(System):
    def __init__(self):
        super().__init__()

        # TODO: Externalize room generation
        self._rooms = {
            0: {
                'name': 'Bridge',
                'exits': [1]
            },
            1: {
                'name': 'Hallway',
                'exits': [1, 2, 3, 4]
            },
            2: {
                'name': 'Engine Room',
                'exits': [1]
            },
            3: {
                'name': 'Quarters',
                'exits': [1, 4]
            },
            4: {
                'name': 'Lounge',
                'exits': [1, 3]
            }
        }

    def run(self):
        ent_with_locations = self._engine.get_matching_entities('location')

        # Refresh nearby_entities
        for entity in self._engine.get_matching_entities('location', 'nearby_entities'):
            self._engine.components['nearby_entities'][entity] = []
            for second_entity in ent_with_locations:
                if self._ec(entity, 'location') == self._ec(second_entity, 'location')\
                        and entity != second_entity:
                    self._engine.components['nearby_entities'][entity].append(second_entity)
