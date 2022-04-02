from systems.gui import GUI
from systems.command_parser import CommandParser


def setup(engine):
    engine.add_system(GUI(), ['GUI_OUTPUT'])
    engine.add_system(CommandParser(), ['GUI_COMMAND'])
