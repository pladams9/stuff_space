from systems.greetings import GreetingsSystem
from systems.gui import GUI
from systems.command_parser import CommandParser
from systems.aging import AgingSystem

def setup(engine):
    engine.add_system(GUI(), ['GUI_OUTPUT'])
    engine.add_system(GreetingsSystem())
    engine.add_system(CommandParser(), ['GUI_COMMAND'])
    engine.add_system(AgingSystem())