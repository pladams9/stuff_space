class System:
    def __init__(self):
        self._engine = None

    def run(self):
        pass


class Engine:
    def __init__(self):
        self._systems = []
        self._components = {}
        self._next_entity_id = 0
        self._running = False

    def get_next_entity_id(self):
        next_id = self._next_entity_id
        self._next_entity_id += 1
        return next_id

    def mainloop(self):
        while self._running:
            self._run_systems()

    def run(self):
        self._running = True
        self.mainloop()

    def shutdown(self):
        self._running = False

    def add_entity(self, properties=None):
        new_id = self.get_next_entity_id()
        for p, v in properties.items():
            if p not in self._components:
                self._components[p] = {}
            self._components[p][new_id] = v

    def add_system(self, system):
        system._engine = self
        self._systems.append(system)

    def get_matching_entities(self, req_props):
        for prop in req_props:
            if prop not in self._components:
                return []

        matching_entities = self._components[req_props[0]].keys()
        for prop in req_props[1:]:
            matching_entities = [entity for entity in matching_entities if entity in self._components[prop]]

        return {entity: {prop: self._components[prop][entity] for prop in req_props} for entity in matching_entities}

    def _run_systems(self):
        for system in self._systems:
            system.run()
