from systems.greetings import GreetingsSystem
from systems.gui import GUI
from systems.command_parser import CommandParser
from systems.aging import AgingSystem
from systems.hunger import HungerSystem

def setup(engine):
    engine.add_system(GUI(), ['GUI_OUTPUT'])
    engine.add_system(GreetingsSystem())
    engine.add_system(CommandParser(), ['GUI_COMMAND'])
    engine.add_system(AgingSystem(), tick_wait=30*365)
    engine.add_system(HungerSystem(), tick_wait=30)
