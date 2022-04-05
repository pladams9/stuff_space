from systems import *


def setup(engine):
    # GUI
    engine.add_system(gui.GUI, engine.GUI_TICK)
    engine.add_system(command_parser.CommandParser, engine.LOGIC_TICK)

    # Timing
    engine.add_system(game_time.GameTimeSystem, engine.LOGIC_TICK)
    engine.add_system(clock_sys.ClockSystem, engine.LOGIC_TICK)

    # Support Systems
    engine.add_system(location.LocationSystem, engine.LOGIC_TICK)

    # Simulation Systems
    engine.add_system(creature_sim.CreatureSimulator, engine.LOGIC_TICK)

    # AI Systems
    engine.add_system(creature_ai.CreatureAI, engine.LOGIC_TICK)

    # Interaction Systems
    engine.add_system(creature_interaction.CreatureInteraction, engine.LOGIC_TICK)
