# IMPORTS
from queue import SimpleQueue
import time


# CLASSES
class System:
    def __init__(self):
        self._engine = None
        self.events = SimpleQueue()

    def run(self):
        pass


class Engine:
    EVERY_TICK = 1
    LOGIC_TICK = 2
    LOGIC_TICK_LENGTH = 1.0 / 30.0
    GUI_TICK = 3
    GUI_TICK_LENGTH = 1.0 / 30.0

    def __init__(self):
        self._systems = {}
        self._systems_by_tick_speed = {
            self.EVERY_TICK: [],
            self.LOGIC_TICK: [],
            self.GUI_TICK: []
        }
        self.time_of_last_logic_tick = time.perf_counter()
        self.time_of_last_gui_tick = time.perf_counter()

        self.components = {}
        self._events = SimpleQueue()
        self._listeners = {}

        self._next_system_id = 0
        self._next_entity_id = 0

        self._running = False

    def _get_next_entity_id(self):
        next_id = self._next_entity_id
        self._next_entity_id += 1
        return next_id

    def _get_next_system_id(self):
        next_id = self._next_system_id
        self._next_system_id += 1
        return next_id

    def mainloop(self):
        while self._running:
            self._handle_events()
            self._run_systems()

    def run(self):
        self._running = True
        self.mainloop()

    def _run_systems(self):
        for system_id in self._systems_by_tick_speed[self.EVERY_TICK]:
            self._systems[system_id].run()

        cur_time = time.perf_counter()
        if cur_time > self.time_of_last_logic_tick + self.LOGIC_TICK_LENGTH:
            self.time_of_last_logic_tick = cur_time
            for system_id in self._systems_by_tick_speed[self.LOGIC_TICK]:
                self._systems[system_id].run()

        if cur_time > self.time_of_last_gui_tick + self.GUI_TICK_LENGTH:
            self.time_of_last_gui_tick = cur_time
            for system_id in self._systems_by_tick_speed[self.GUI_TICK]:
                self._systems[system_id].run()

    def _handle_events(self):
        while not self._events.empty():
            e = self._events.get()

            if e[0] == 'SYSTEM_COMMAND':
                self._handle_system_command(e)

            if e[0] in self._listeners:
                for listener in self._listeners[e[0]]:
                    self._systems[listener].events.put(e)

    def _handle_system_command(self, e):
        if e[1] == 'shutdown':
            self.shutdown()
        elif e[1][0] == 'set_tick_length':
            self.LOGIC_TICK_LENGTH = e[1][1]

    def shutdown(self):
        self._running = False

    def add_system(self, system, tick_type, listening_to=None):
        system._engine = self
        new_id = self._get_next_system_id()
        self._systems[new_id] = system

        if listening_to is not None:
            for event_type in listening_to:
                self._add_listener(new_id, event_type)

        if tick_type == Engine.EVERY_TICK:
            self._systems_by_tick_speed[self.EVERY_TICK].append(new_id)
        elif tick_type == Engine.LOGIC_TICK:
            self._systems_by_tick_speed[self.LOGIC_TICK].append(new_id)
        elif tick_type == Engine.GUI_TICK:
            self._systems_by_tick_speed[self.GUI_TICK].append(new_id)

    def _add_listener(self, system_id, event_type):
        if event_type not in self._listeners:
            self._listeners[event_type] = []
        self._listeners[event_type].append(system_id)

    def fire_event(self, event=('NullEventType', 'NoData')):
        self._events.put(event)

    def add_entity(self, components):
        new_id = self._get_next_entity_id()
        for c, v in components.items():
            if c not in self.components:
                self.components[c] = {}
            self.components[c][new_id] = v

    def remove_entity(self, entity_id):
        for component in self.components:
            self.components[component].pop(entity_id, None)

    def get_matching_entities(self, req_props):
        for prop in req_props:
            if prop not in self.components:
                return ()

        matching_entities = self.components[req_props[0]].keys()
        for prop in req_props[1:]:
            matching_entities = [entity for entity in matching_entities if entity in self.components[prop]]

        return tuple(matching_entities)

    def get_all_entities(self):
        entities = []
        for component in self.components.values():
            for entity in component.keys():
                if entity not in entities:
                    entities.append(entity)

        return tuple(entities)

    def get_entity_components(self, entity_id):
        return_comps = {}
        for component, entities in self.components.items():
            if entity_id in entities:
                return_comps[component] = self.components[component][entity_id]

        return return_comps
