import PySimpleGUI as sg


class Hangman:
    def __init__(self) -> None:
        self.window = sg.Window(
            title="Hangman",
            layout=[[]],
            finalize=True,
            margins=(100, 100),
        )

    def read_event(self):
        event = self.window.read()
        event_id = event[0] if event is not None else None
        return event_id

    def close(self):
        self.window.close()


if __name__ == '__main__':
    game = Hangman()
    # event loop
    while True:
        event_id = game.read_event()
        if event_id in {sg.WIN_CLOSED}:
            break
    game.close()
