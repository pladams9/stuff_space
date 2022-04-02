from systems import *


def setup(engine):
    engine.add_system(gui.GUI(), engine.GUI_TICK, ['GUI_OUTPUT'],)
    engine.add_system(command_parser.CommandParser(), engine.LOGIC_TICK, ['GUI_COMMAND'])
    engine.add_system(game_time.GameTimeSystem(), engine.LOGIC_TICK)
    engine.add_system(creature_sim.CreatureSimulator(), engine.LOGIC_TICK)
