from engine import System


class LocationSystem(System):
    def __init__(self):
        super().__init__()

    def run(self):
        ent_with_locations = self._engine.get_matching_entities('location')

        # Refresh nearby_entities
        for entity in self._engine.get_matching_entities('location', 'nearby_entities'):
            self._engine.components['nearby_entities'][entity] = []
            for second_entity in ent_with_locations:
                if self._engine.components['location'][entity] == self._engine.components['location'][second_entity]\
                        and entity != second_entity:
                    self._engine.components['nearby_entities'][entity].append(second_entity)
