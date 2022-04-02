from engine import System


class CreatureSimulator(System):
    def __init__(self):
        super().__init__()

    def run(self):
        entities = self._engine.get_matching_entities('creature')
        for entity in entities:
            # TODO: Add simulation functions
            self._engine.components['creature'][entity]['age'] += 1
