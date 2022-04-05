from engine import System
import tkinter as tk
import tkinter.font as tkfont
import time


class GUI(System):
    LISTENERS = ['GUI_OUTPUT']

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

        # Terminal Text Tags
        self._terminal.tag_configure('text', foreground='#AAA')
        self._terminal.tag_configure('highlight', foreground="#67F")
        self._terminal.tag_configure('command', foreground='#FFF')
        self._terminal.tag_configure('error', foreground='#00F')
        self._terminal.tag_configure('critical', background='#00F', foreground="#FFF")
        self._terminal.tag_configure('sel', background='#44A', foreground="#CCC")
        self._terminal.tag_raise('sel')

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

        self._CMD_LINE_MAX_HISTORY = 100
        self._cmd_line_history = []
        self._cmd_line_history_pos = -1

        self._cmd_line.bind('<Return>', self._submit_cmd)
        self._cmd_line.bind('<Key-Up>', self._cmd_line_scroll)
        self._cmd_line.bind('<Key-Down>', self._cmd_line_scroll)

        self._cmd_line.focus()

        def terminal_type(e):
            if e.state == 4 and e.keysym == 'c':
                return None
            else:
                self._cmd_line.focus()
                if len(e.keysym) == 1:
                    self._cmd_line.event_generate(e.keysym)
                return 'break'

        self._terminal.bind("<Key>", terminal_type)

    def run(self):
        cur_scroll_end = self._terminal.yview()[1]

        self._handle_events()

        if cur_scroll_end == 1.0:
            self._terminal.yview_moveto(1.0)

        self._window.update()  # Processes all outstanding events on this tick

    def _handle_event(self, e):
        if e[0] == 'GUI_OUTPUT':
            self._terminal.insert('end', e[1][0], e[1][1])
            self._terminal.insert('end', '\n')

    def _submit_cmd(self, _e):
        self._engine.fire_event(('GUI_INPUT', self._cmd_line.get()))

        if len(self._cmd_line_history) == 0 or self._cmd_line.get() != self._cmd_line_history[0]:
            self._cmd_line_history.insert(0, self._cmd_line.get())
        if len(self._cmd_line_history) > self._CMD_LINE_MAX_HISTORY:
            self._cmd_line_history.pop()
        self._cmd_line_history_pos = -1

        self._cmd_line.delete(0, 'end')

    def _cmd_line_scroll(self, e):
        scrolled = False
        if e.keysym == 'Up' \
                and len(self._cmd_line_history) > 0 \
                and self._cmd_line_history_pos < self._CMD_LINE_MAX_HISTORY \
                and self._cmd_line_history_pos < len(self._cmd_line_history) - 1:
            self._cmd_line_history_pos += 1
            scrolled = True
        elif e.keysym == 'Down' \
                and self._cmd_line_history_pos > 0:
            self._cmd_line_history_pos -= 1
            scrolled = True

        if scrolled:
            self._cmd_line.delete(0, 'end')
            self._cmd_line.insert(0, self._cmd_line_history[self._cmd_line_history_pos])

    def _close(self):
        self._engine.fire_event(('SYSTEM_COMMAND', 'shutdown'))
