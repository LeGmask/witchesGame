from enum import IntEnum


class Move(IntEnum):
    LEFT = -1
    UP = -3
    RIGHT = 1
    DOWN = 3


class InvalidDirectionError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class GameBoard:
    def __init__(self, cards) -> None:
        self.board = cards

    def check(self):
        errors = 0
        # Here we need to check if the sum of 2 adjacent edges is equal to 9
        for i in range(2):
            for j in range(3):
                # Firstly we check for the vertical adjacent edges
                errors += (
                    0
                    if self.board[j * 3 + i].getRight()
                    + self.board[j * 3 + i + 1].getLeft()
                    == 9
                    else 1
                )
                # Secondly we check for the vertical adjacent edges
                errors += (
                    0
                    if self.board[j + i * 3].getDown()
                    + self.board[j + i * 3 + 3].getUp()
                    == 9
                    else 1
                )

        return errors

    def move(self, i: int, deplacement: Move):
        line = i // 3
        if (
            deplacement in [Move.RIGHT, Move.LEFT]
            and i - line * 3 + int(deplacement) >= 0
        ) or i + int(deplacement) >= 0:
            # fmt: off
            self.board[i], self.board[i + int(deplacement)] = self.board[i + int(deplacement)], self.board[i]
            # fmt: on
        else:
            raise InvalidDirectionError()

    def toString(self):
        string = ""
        for i in range(3):
            for j in range(3):  # UP
                string += f" {self.board[i*3 + j].getUp()}  "
            string += "\n"
            for j in range(3):  # Sides
                string += (
                    f"{self.board[i*3 + j].getLeft()}+{self.board[i*3 + j].getRight()} "
                )
            string += "\n"
            for j in range(3):  # Down
                string += f" {self.board[i*3 + j].getDown()}  "
            string += "\n\n"

        return string

    def toArray(self):
        return [card.sides for card in self.board]
