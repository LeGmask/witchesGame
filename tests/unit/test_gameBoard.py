import pytest
from src.card import *
from src.gameBoard import *


class TestGameBoard:
    # We should disable black autoformating here, since that put the card in this way is way easier to understand actual gameboard
    # fmt: off
    cards = [
        Card(5, 1, 2, 7), Card(7, 3, 2, 8), Card(7, 6, 2, 3),
        Card(5, 2, 4, 8), Card(5, 1, 3, 7), Card(6, 6, 4, 1),
        Card(8, 1, 2, 7), Card(7, 2, 3, 5), Card(6, 8, 2, 1)
    ]
    # fmt: on
    cards_sides = [card.sides for card in cards]
    gameBoard = GameBoard(cards)

    def test_create_gameBoard(self):
        assert self.gameBoard.board == self.cards

    def test_gameBoard_check(self):
        # Here we test if the gameboard is sucessfull, since the cards entry is valid, it should be valid here too
        assert (
            self.gameBoard.check() == 0
        ), "cards used to init gameBoard is valid, expecting 0 errors"

    def test_gameBoard_move(self):
        # To move a card, we should : give the card id, and select the direction using Move enum:
        self.gameBoard.move(0, Move.DOWN)
        # We should disable black autoformating here, since that put the card in this way is way easier to understand actual gameboard
        # fmt: off
        assert self.gameBoard.toArray() == [
            Card(5, 2, 4, 8).sides, Card(7, 3, 2, 8).sides, Card(7, 6, 2, 3).sides,
            Card(5, 1, 2, 7).sides, Card(5, 1, 3, 7).sides, Card(6, 6, 4, 1).sides,
            Card(8, 1, 2, 7).sides, Card(7, 2, 3, 5).sides, Card(6, 8, 2, 1).sides
        ]
        # fmt: on

        self.gameBoard.move(3, Move.UP)
        assert self.gameBoard.toArray() == self.cards_sides

        self.gameBoard.move(0, Move.RIGHT)
        # We should disable black autoformating here, since that put the card in this way is way easier to understand actual gameboard
        # fmt: off
        assert self.gameBoard.toArray() == [
            Card(7, 3, 2, 8).sides, Card(5, 1, 2, 7).sides, Card(7, 6, 2, 3).sides,
            Card(5, 2, 4, 8).sides, Card(5, 1, 3, 7).sides, Card(6, 6, 4, 1).sides,
            Card(8, 1, 2, 7).sides, Card(7, 2, 3, 5).sides, Card(6, 8, 2, 1).sides
        ]
        # fmt: on

        self.gameBoard.move(1, Move.LEFT)
        assert self.gameBoard.toArray() == self.cards_sides

        # Now we should try to move a card in the edges of the gameBoard
        # Since it's impossible, this should raise a new exception
        with pytest.raises(InvalidDirectionError):
            self.gameBoard.move(0, Move.UP)
            self.gameBoard.move(0, Move.LEFT)

            self.gameBoard.move(1, Move.UP)

            self.gameBoard.move(2, Move.UP)
            self.gameBoard.move(2, Move.RIGHT)

            self.gameBoard.move(3, Move.LEFT)

            self.gameBoard.move(5, Move.RIGHT)

            self.gameBoard.move(6, Move.LEFT)
            self.gameBoard.move(6, Move.DOWN)

            self.gameBoard.move(7, Move.DOWN)

            self.gameBoard.move(8, Move.RIGHT)
            self.gameBoard.move(8, Move.DOWN)

    def test_gameBoard_toString(self):
        assert (
            self.gameBoard.toString()
            == " 1   3   6  \n5+2 7+2 7+2 \n 7   8   3  \n\n 2   1   6  \n5+4 5+3 6+4 \n 8   7   1  \n\n 1   2   8  \n8+2 7+3 6+2 \n 7   5   1  \n\n"
        )
