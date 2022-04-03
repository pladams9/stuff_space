from engine import System


class CreatureInteraction(System):
    LISTENERS = ['CREATURE_INTERACTION']

    def __init__(self):
        super().__init__()

    def _handle_event(self, e):
        # TODO: Break out this function into a separate module. One for every type of interaction. Have the modules register for the interaction type they want to handle.
        if e[1]['type'] == 'attack':
            target_creature = self._engine.components['creature'][e[1]['target']]
            if target_creature['alive']:
                self._engine.components['creature'][e[1]['target']]['health'] -= 0.1
                self._engine.fire_event((
                    'GUI_OUTPUT',
                    (f"{self._engine.components['name'][e[1]['primary']]} attacked {self._engine.components['name'][e[1]['target']]}!", 'text')
                ))
