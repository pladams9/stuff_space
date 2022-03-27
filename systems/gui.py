from engine import System
import tkinter as tk


class GUI(System):
    def __init__(self):
        super().__init__()

        self._window = tk.Tk()

        self._terminal = tk.Text()
        self._cmd_line = tk.Entry()

        self._terminal.pack()
        self._cmd_line.pack()

    def run(self):
        entities = self._engine.get_matching_entities(['output'])

        try:
            for entity, props in entities.items():
                for line in props['output']:
                    self._terminal.insert('end', line)
                    self._terminal.insert('end', '\n')
                self._engine._components['output'][entity].clear() # TODO: Move this to an output clearing system
                # TODO: Remove direct access to components

            self._window.update()
        except tk.TclError as err:
            self._engine.shutdown() # TODO: Capture window close instead of doing this by exception
