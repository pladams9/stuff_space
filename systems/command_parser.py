from engine import System


class CommandParser(System):
    def __init__(self):
        super().__init__()

    def run(self):
        while not self.events.empty():
            e = self.events.get()
            self._engine.fire_event(('GUI_OUTPUT', ('> ' + e[1], 'command')))

            # Parse
            if e[1] in ('shutdown', 'exit', 'quit'):
                self._engine.fire_event(('SYSTEM_COMMAND', 'shutdown'))

            if e[1] == 'sing a song':
                self._engine.fire_event(('GUI_OUTPUT', ('La dee da dee la dee da...', 'highlight')))

            if e[1] in ('print entities', 'pe'):
                for entity in self._engine.get_all_entities():
                    self._engine.fire_event((
                        'GUI_OUTPUT',
                        (
                            f"{entity}: {self._engine.get_entity_components(entity)}",
                            'text'
                        )
                    ))

            if e[1].startswith('set tick length '):
                try:
                    new_tick_length = float(e[1][16:])
                    self._engine.fire_event(('SYSTEM_COMMAND', ('set_tick_length', new_tick_length)))
                except ValueError:
                    self._engine.fire_event(('GUI_OUTPUT', (f"Could not understand tick length value: {e[1][16:]}", 'error')))
