from . import interaction_handlers as ih


def attack(self, e):
    target_creature = self._ec(e[1]['target'], 'creature')
    if target_creature['alive']:
        self._ec(e[1]['target'], 'creature')['health'] -= 0.1
        self._engine.fire_event((
            'GUI_OUTPUT',
            (f"{self._ec(e[1]['primary'], 'name')} attacked {self._ec(e[1]['target'], 'name')}!", 'text')
        ))


ih.INTERACTION_HANDLERS['attack'] = attack
