from engine import System


class MannaSystem(System):
    def __init__(self):
        super().__init__()
        self.ticks_since_last = 0

    def run(self):
        self.ticks_since_last += 1
        entities = self._engine.get_matching_entities(['food'])
        if len(entities) < 5 and self.ticks_since_last > 2:
            self._engine.add_entity({
                'food': True
            })
            self.ticks_since_last = 0
