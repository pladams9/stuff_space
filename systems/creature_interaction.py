from engine import System


class CreatureInteraction(System):
    LISTENERS = ['CREATURE_INTERACTION']

    def __init__(self):
        super().__init__()

    def _handle_event(self, e):
        if e[1]['type'] == 'attack':
            pass
