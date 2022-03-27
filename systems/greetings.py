from engine import System


class GreetingsSystem(System):
    def __init__(self):
        super().__init__()

    def run(self):
        entities = self._engine.get_matching_entities(['name', 'greeting', 'output'])
        for entity, props in entities.items():
            self._engine._components['output'][entity].append(f"{props['name']} says \"{props['greeting']}\"")
            # TODO: Remove direct access to components