from engine import System


class CreatureAISystem(System):
    def __init__(self):
        super().__init__()

    def run(self):
        creatures = self._engine.get_matching_entities(['creature', 'satiety'])
        for creature in creatures:
            food = self._engine.get_matching_entities(['food'])
            if self._engine.components['satiety'][creature] <= 0.5 and len(food) > 0:
                self._engine.components['satiety'][creature] += 0.25
                self._engine.remove_entity(food[0])
                self._engine.fire_event((
                    'GUI_OUTPUT',
                    (
                        f"{self._engine.components['name'][creature]} ate some food.",
                        'text'
                    )
                ))