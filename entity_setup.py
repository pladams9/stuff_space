import entities as ent


def setup(engine):
    engine.add_entity(ent.creatures.dinosaur())
    engine.add_entity(ent.creatures.dinosaur())
