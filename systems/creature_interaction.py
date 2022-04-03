from engine import System
from systems.creature_interactions import interaction_handlers as ih


class CreatureInteraction(System):
    LISTENERS = ['CREATURE_INTERACTION']

    def __init__(self):
        super().__init__()

    def _handle_event(self, e):
        if e[1]['type'] in ih.INTERACTION_HANDLERS:
            ih.INTERACTION_HANDLERS[e[1]['type']](self, e)
