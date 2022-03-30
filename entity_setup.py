import random as r


def setup(engine):
    engine.add_entity({
        'name': 'Alice',
        'creature': True,
        'age': r.randint(0, 10),
        'satiety': 0.5 + (r.random() * 0.5)
    })
    engine.add_entity({
        'name': 'Bob',
        'creature': True,
        'age': r.randint(0, 10),
        'satiety': 0.5 + (r.random() * 0.5)
    })
    engine.add_entity({
        'name': 'Charlie',
        'creature': True,
        'age': r.randint(0, 10),
        'satiety': 0.5 + (r.random() * 0.5)
    })
