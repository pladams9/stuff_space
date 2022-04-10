from engine import System


class LocationSystem(System):
    LISTENERS = ['LOCATION_MOVE']

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
                'exits': [0, 2, 3, 4]
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
        # Refresh nearby_entities
        for entity in self._engine.get_matching_entities('location', 'nearby_entities'):
            self._refresh_nearby_entities(entity)

        # Refresh exits
        for entity in self._engine.get_matching_entities('location'):
            self._refresh_exits(entity)

        # Handle events
        self._handle_events()

    def _handle_event(self, e):
        if e[0] == 'LOCATION_MOVE':
            if e[1]['destination'] in self._rooms[self._ec(e[1]['entity'], 'location')['room_id']]['exits']:
                self._engine.components['location'][e[1]['entity']]['room_id'] = e[1]['destination']
                self._refresh_nearby_entities(e[1]['entity'])
                self._refresh_exits(e[1]['entity'])
                self._engine.fire_event((
                    'GUI_OUTPUT',
                    (f"{self._ec(e[1]['entity'], 'name')} moved to {self._rooms[e[1]['destination']]['name']}.", 'text')
                ))

    def _refresh_nearby_entities(self, entity):
        self._engine.components['nearby_entities'][entity] = []
        for second_entity in self._engine.get_matching_entities('location'):
            if self._ec(entity, 'location')['room_id'] == self._ec(second_entity, 'location')['room_id'] \
                    and entity != second_entity:
                self._engine.components['nearby_entities'][entity].append(second_entity)

    def _refresh_exits(self, entity):
        self._engine.components['location'][entity]['exits'] = self._rooms[self._ec(entity, 'location')['room_id']][
            'exits']
