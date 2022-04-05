from engine import System
from utils.pretty_dict_string import to_pretty_str


class CommandParser(System):
    LISTENERS = ['GUI_INPUT']

    def __init__(self):
        super().__init__()

    def _handle_event(self, e):
        self._engine.fire_event(('GUI_OUTPUT', ('> ' + e[1], 'command')))
        # TODO: Print unsuccessful commands as invalid

        # Parse
        # TODO: Break these out into separate functions? Use a dict to parcel out things?

        if e[1] in ('shutdown', 'exit', 'quit'):
            self._engine.fire_event(('SYSTEM_COMMAND', 'shutdown'))

        if e[1] in ('print entities', 'pe'):
            # TODO: Allow subsets of entities, e.g. 'print entities creature' or 'print entities location'
            for entity in self._engine.get_all_entities():
                self._engine.fire_event((
                    'GUI_OUTPUT',
                    (
                        f"{entity}:\n{to_pretty_str(self._engine.get_entity_components(entity), 4)}",
                        'text'
                    )
                ))

        if e[1].startswith('set tick length '):
            # TODO: make this work with different types of ticks
            try:
                new_tick_length = float(e[1][16:])
                self._engine.fire_event(('SYSTEM_COMMAND', ('set_tick_length', new_tick_length)))
            except ValueError:
                self._engine.fire_event(('GUI_OUTPUT', (f"Could not understand tick length value: {e[1][16:]}", 'error')))
