from systems.greetings import GreetingsSystem
from systems.ages import AgeSystem
from systems.gui import GUI


def setup(engine):
    engine.add_system(GUI())
    engine.add_system(GreetingsSystem())
    engine.add_system(AgeSystem())
