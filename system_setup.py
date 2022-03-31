from systems.gui import GUI
from systems.command_parser import CommandParser
from systems.aging import AgingSystem
from systems.hunger import HungerSystem
from systems.death import DeathSystem
from systems.manna import MannaSystem
from systems.creature_ai import CreatureAISystem


def setup(engine):
    engine.add_system(GUI(), ['GUI_OUTPUT'])
    engine.add_system(CommandParser(), ['GUI_COMMAND'])
    engine.add_system(AgingSystem(), tick_wait=300)
    engine.add_system(HungerSystem(), tick_wait=30)
    engine.add_system(DeathSystem(), tick_wait=30)
    engine.add_system(MannaSystem(), tick_wait=30)
    engine.add_system(CreatureAISystem(), tick_wait=30)