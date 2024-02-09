import PySimpleGUI as sg
from string import ascii_lowercase


class Hangman:
    def __init__(self) -> None:
        layout = [
            [self._build_canvas_frame(), self._build_canvas_frame(),
             ],
            [
                self._build_guessed_word_frame(),
            ],
            [
                self._build_guessed_word_frame(),
            ],
        ]
        self._window = sg.Window(
            title="Hangman",
            finalize=True,
            margins=(100, 100),
        )
    # build canvas frame method

    def _build_canvas_frame(self):
        return sg.Frame(
            "Hangman",
            [
                [
                    sg.Graph(
                        key="-CANVAS-",
                        canvas_size=(200, 400),
                        graph_bottom_left=(0, 0),
                        graph_top_right=(200, 400),
                    )
                ]
            ],
            font="Any 20",
        )
    # build letters frame

    def _build_letters_frame(self):
        letter_groups = [
            ascii_uppercase[i:i + 4] for i in range(0, len(ascii_uppercase), 4)
        ]
        letter_buttons = [
            [
                sg.Button(
                    button_text=f"{letter}",
                    font="Courier 20",
                    border_width=4,
                    button_color=(None, sg.theme_background_color()),
                    key=f"-LETTER-{letter}",
                    enable_events=True,
                )
                for letter in letter_group
            ]
            for letter_group in letter_groups
        ]
        return sg.Column(
            [
                [
                    sg.Frame(
                        "Letters",
                        letter_buttons,
                        font="Any 20",
                    ),
                    sg.Sizer(),
                ]
            ]
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
