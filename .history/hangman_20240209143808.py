import PySimpleGUI as sg
from string import ascii_uppercase

MAX_WRONG_GUESSES = 6


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
            layout=layout,
            finalize=True,
        )
    # build canvas frame method
        self._canvas = self._window["-CANVAS-"]

    # draw scaffold
        self._draw_scaffold()
        for index in range(MAX_WRONG_GUESSES):
            self._wrong_guesses = index + 1
            self._draw_hanged_man()

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
                    border_width=0,
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
    # build guessed word frame

    def _build_guessed_word_frame(self):
        return sg.Frame(
            "",
            [
                [
                    sg.Text(
                        key="-DISPLAY-WORD-",
                        font="Courier 20",
                    )
                ]
            ],
            element_justification="center",
        )
    # build action buttons

    def _build_action_buttons(self):
        return sg.Frame(
            "",
            [
                [
                    sg.Sizer(h_pixels=90),
                    sg.Button(
                        button_text="New",
                        key="-NEW-",
                        font="Any 20",
                    ),
                    sg.Sizer(h_pixels=90),
                    sg.Button(
                        button_text="Restart",
                        key="-RESTART-",
                        font="Any 20",
                    ),
                    sg.Sizer(h_pixels=90),
                    sg.Button(
                        button_text="Quit",
                        key="-QUIT-",
                        font="Any 20",
                    ),
                    sg.Sizer(h_pixels=90),
                ]
            ],
            font="Any 20",
        )

    def read_event(self):
        event = self._window.read()
        event_id = event[0] if event is not None else None
        return event_id

    def close(self):
        self._window.close()

    def _draw_scaffold(self):
        lines = [
            ((40, 55), (180, 55), 10),
            ((165, 60), (165, 365), 10),
            ((160, 360), (100, 360), 10),
            ((100, 365), (100, 330), 10),
            ((100, 330), (100, 310), 1),
        ]
        for *points, width in lines:
            self._canvas.DrawLine(*points, color="black", width=width)

    # draw hanged man
    def _draw_hanged_man(self):
        head = (100, 290)
        torso = [(100, 270), (100, 170)]
        left_arm, right_arm = [
            ((100, 250), (80, 250)),
            ((80, 250), (60, 210)),
            ((60, 210), (60, 190))
        ], [
            ((100, 250), (120, 250)),
            ((120, 250), (140, 220)),
            ((140, 220), (140, 190)),
        ]
        left_leg, right_leg = [
            ((100, 170), (80, 140)),
            ((80, 140), (60, 110)),
            ((60, 110), (60, 90))
        ], [
            ((100, 170), (120, 140)),
            ((120, 140), (140, 110)),
            ((140, 110), (140, 90))
        ]
        body = [
            torso,
            left_arm,
            right_arm,
            left_leg,
            right_leg
        ]
        if self._wrong_guesses == 1:
            self._canvas.DrawCircle(head, 20, fill_color="red", line_width=2)
        elif self._wrong_guesses > 1:
            for part in body[:self._wrong_guesses-2]:
                for line in part:
                    self._canvas.DrawLine(*line, color="black", width=2)


...
if __name__ == '__main__':
    game = Hangman()
    # event loop
    while True:
        event_id = game.read_event()
        if event_id in {sg.WIN_CLOSED}:
            break
    game.close()
