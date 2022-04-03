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
            if not self._engine.components['creature'][entity]['alive']:
                continue

            # Health
            if self._engine.components['creature'][entity]['health'] <= 0.0:
                self._engine.components['creature'][entity]['health'] = 0.0
                self._engine.components['creature'][entity]['alive'] = False
                self._engine.fire_event((
                    'GUI_OUTPUT',
                    (f"{self._engine.components['name'][entity]} died.", 'text')
                ))
                # TODO: Separate strings into their own system?
                # TODO: Maybe this is the History and StoryTelling systems. They receive events and store/output those events respectively.
                # TODO: So we need an event for the death.

            # Aging
            if new_day:
                self._engine.components['creature'][entity]['age'] += 1

