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


if __name__ == '__main__':
    game = Hangman()
    # event loop
    while True:
        event = game.read_event()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
    game.close()
