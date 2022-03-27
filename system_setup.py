from systems.greetings import GreetingsSystem
from systems.ages import AgeSystem


def setup(engine):
    engine.add_system(GreetingsSystem())
    engine.add_system(AgeSystem())
