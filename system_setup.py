from systems.gui import GUI
from systems.command_parser import CommandParser
from systems.calendar import CalendarSystem

def setup(engine):
    engine.add_system(GUI(), engine.GUI_TICK, ['GUI_OUTPUT'],)
    engine.add_system(CommandParser(), engine.LOGIC_TICK, ['GUI_COMMAND'])
    engine.add_system(CalendarSystem(), engine.LOGIC_TICK)
