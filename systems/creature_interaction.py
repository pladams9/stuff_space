from engine import System


class CreatureInteraction(System):
    LISTENERS = ['CREATURE_INTERACTION']

    def __init__(self):
        super().__init__()

    def _handle_event(self, e):
        # TODO: Break out this function into a separate module. One for every type of interaction. Have the modules register for the interaction type they want to handle.
        if e[1]['type'] == 'attack':
            target_creature = self._ec(e[1]['target'], 'creature')
            if target_creature['alive']:
                self._ec(e[1]['target'], 'creature')['health'] -= 0.1
                self._engine.fire_event((
                    'GUI_OUTPUT',
                    (f"{self._ec(e[1]['primary'], 'name')} attacked {self._ec(e[1]['target'], 'name')}!", 'text')
                ))
