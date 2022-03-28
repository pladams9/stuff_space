from engine import System


class CommandParser(System):
    def __init__(self):
        super().__init__()

    def run(self):
        while not self.events.empty():
            e = self.events.get()
            self._engine.fire_event(('GUI_OUTPUT', ('> ' + e[1], 'command')))
            if e[1] in ('shutdown', 'exit', 'quit'):
                self._engine.fire_event(('SYSTEM_COMMAND', 'shutdown'))

            if e[1] == 'sing a song':
                self._engine.fire_event(('GUI_OUTPUT', ('La dee da dee la dee da...', 'highlight')))

            if e[1] in ('print entities', 'pe'):
                for entity in self._engine.get_matching_entities(['creature']):
                    self._engine.fire_event((
                        'GUI_OUTPUT',
                        (
                            str(self._engine.get_entity_components(entity)),
                            'text'
                        )
                    ))
