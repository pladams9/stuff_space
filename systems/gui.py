from engine import System
import tkinter as tk
import tkinter.font as tkfont


class GUI(System):
    def __init__(self):
        super().__init__()

        # Main Window
        self._window = tk.Tk()
        self._window.geometry('800x400')
        self._window.grid_columnconfigure(0, weight=1)
        self._window.grid_columnconfigure(1, weight=0)
        self._window.grid_rowconfigure(0, weight=1)
        self._window.grid_rowconfigure(1, weight=0)
        self._window.configure(
            background='#555'
        )
        self._window.title('Stuff Space')
        self._window.protocol("WM_DELETE_WINDOW", self._close)

        # Terminal
        self._terminal = tk.Text()
        self._terminal.configure(
            background='#000',
            foreground='#FFF',
            relief='flat',
            spacing3=8,
            wrap='word'
        )
        self._terminal.grid(column=0, row=0, sticky='nesw')

        def prevent_editing(e):
            if e.state == 4 and e.keysym == 'c':
                return None
            else:
                return 'break'
        self._terminal.bind("<Key>", prevent_editing)

        # Terminal Scrollbar
        self._scrollbar = tk.Scrollbar()
        self._scrollbar.configure(command=self._terminal.yview)
        self._scrollbar.grid(column=1, row=0, sticky='ns')
        self._terminal.configure(yscrollcommand=self._scrollbar.set)

        # Terminal Command Line
        self._cmd_line = tk.Entry()
        self._cmd_line.configure(
            background='#000',
            foreground='#FFF',
            insertbackground='#FFF',
            relief='flat',
            font=tkfont.Font(
                family='Courier',
                size=11
            )
        )
        self._cmd_line.grid(column=0, row=1, columnspan=2, sticky='ew', padx=3, pady=3)
        self._cmd_line.bind('<Return>', self._submit_cmd)
        self._cmd_line.focus()

    def run(self):
        cur_scroll_end = self._terminal.yview()[1]

        while not self.events.empty():
            e = self.events.get()
            if e[0] == 'GUI_OUTPUT':
                self._terminal.insert('end', e[1])
                self._terminal.insert('end', '\n')

        if cur_scroll_end == 1.0:
            self._terminal.yview_moveto(1.0)

        self._window.update()

    def _submit_cmd(self, e):
        self._engine.fire_event(('GUI_COMMAND', self._cmd_line.get()))
        self._cmd_line.delete(0, 'end')

    def _close(self):
        self._engine.fire_event(('SYSTEM_COMMAND', 'shutdown'))
