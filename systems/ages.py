from engine import System


class AgeSystem(System):
    def __init__(self):
        super().__init__()

    def run(self):
        entities = self._engine.get_matching_entities(['name', 'age'])
        for entity, properties in entities.items():
            print(f"{properties['name']} is {properties['age']} years old.")
