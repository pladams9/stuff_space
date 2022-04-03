from engine import System


class CreatureSimulator(System):
    LISTENERS = ['TIME_NEW_DAY']

    def __init__(self):
        super().__init__()

    def run(self):
        new_day = False
        while not self.events.empty():
            e = self.events.get()
            if e[0] == 'TIME_NEW_DAY':
                new_day = True

        entities = self._engine.get_matching_entities('creature')
        for entity in entities:
            # Aging
            if new_day:
                self._engine.components['creature'][entity]['age'] += 1
