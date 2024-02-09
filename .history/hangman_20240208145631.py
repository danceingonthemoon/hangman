import PySimpleGUI as sg


class Hangman:
    def __init__(self) -> None:
        self.window = sg.Window('Hangman', self.layout())
        title = 'Hangman'
        layout = []
        finalize = True
        margins = (0, 0)

    def read_event(self):
        event = self.window.read()
        return event[0] if event is not None else None

    def close(self):
        self.window.close()
