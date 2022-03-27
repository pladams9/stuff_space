from engine import System


class AgeSystem(System):
    def __init__(self):
        super().__init__()

    def run(self):
        entities = self._engine.get_matching_entities(['name', 'age', 'output'])
        for entity, props in entities.items():
            self._engine._components['output'][entity].append(f"{props['name']} is {props['age']} years old.")
            # TODO: Remove direct access to components