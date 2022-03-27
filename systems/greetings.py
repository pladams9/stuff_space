from engine import System


class GreetingsSystem(System):
    def __init__(self):
        super().__init__()

    def run(self):
        entities = self._engine.get_matching_entities(['name', 'greeting'])
        for entity, properties in entities.items():
            print(f"{properties['name']} says \"{properties['greeting']}\"")
