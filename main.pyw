# IMPORTS
import engine
import system_setup
import entity_setup

app = engine.Engine()

system_setup.setup(app)

entity_setup.setup(app)

app.run()
