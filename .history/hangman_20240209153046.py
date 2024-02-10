import PySimpleGUI as sg
from string import ascii_uppercase
from random import choice

MAX_WRONG_GUESSES = 6


class Hangman:
    def __init__(self) -> None:
        layout = [
            [self._build_canvas_frame(), self._build_letters_frame(),
             ],
            [
                self.  # The `_build_guessed_word_frame` method is responsible for creating the frame
                # that displays the guessed word in the Hangman game. It creates a frame with a
                # single text element that will be updated with the current state of the guessed
                # word.
                _build_guessed_word_frame(),
            ],
            [
                self._build_action_buttons_frame(),
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
            ascii_uppercase[i: i + 4] for i in range(0, len(ascii_uppercase), 4)
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

    def _build_action_buttons_frame(self):
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
        left_arm = [
            ((100, 250), (80, 250)),
            ((80, 250), (60, 210)),
            ((60, 210), (60, 190))
        ]
        right_arm = [
            ((100, 250), (120, 250)),
            ((120, 250), (140, 210)),
            ((140, 210), (140, 190)),
        ]

        left_leg = [
            ((100, 170), (80, 170)),
            ((80, 170),  (70, 140)),
            ((70, 140),  (70,  90)),
            ((70, 80),   (60, 80)),
        ]
        right_leg = [
            ((100, 170), (120, 170)),
            ((120, 170), (130, 140)),
            ((130, 140), (140, 90)),
            ((130, 80),  (140, 80)),
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
                    self._canvas.DrawLine(*line, color="red", width=2)

        self._draw_scaffold()
        for index in range(MAX_WRONG_GUESSES):
            self._wrong_guesses = index + 1
            self._draw_hanged_man()

    def _select_word(self):
        with open("words.txt", "r") as file:
            words_list = file.readlines()
        return choice(words_list).strip().upper()

    # track the guessed word
    def _build_guessed_word(self):
        current_words = []
        for letter in self._target_word:
            if letter in self._guessed_word:
                current_words.append(letter)
            else:
                current_words.append("_")

        return " ".join(current_words)

    def __new__game(self):
        self._target_word = self._select_word()
        self._restart_game()

    def _restart_game(self):
        self._guessed_word = set()
        self._wrong_guesses = 0
        self._guessed_word = self._build_guessed_word()

        # restart GUI
        self._canvas.erase()
        self._draw_scaffold()
        for letter in ascii_uppercase:
            self._window[f"-LETTER-{letter}"].update(disabled=False)
        self.window["-DISPLAY-WORD-"].update(self._guessed_word)


if __name__ == '__main__':
    game = Hangman()
    # event loop
    while True:
        event_id = game.read_event()
        if event_id in {sg.WIN_CLOSED}:
            break
    game.close()
