from src.card import *


class TestCard:
    card = Card(7, 8, 3, 4) # we use an attributes to avoid recreate a card instance for each test

    def test_create_card(self):
        assert self.card.sides == [7, 8, 3, 4]

    def test_card_tostring(self):
        assert self.card.toString() == "7, 8, 3, 4"

    def test_card_rotation(self):
        self.card.rotation()
        assert self.card.sides == [4, 7, 8, 3]
        assert self.card.rotation_count == 1
        self.card.rotation()
        assert self.card.sides == [3, 4, 7, 8]
        assert self.card.rotation_count == 2
        self.card.rotation()
        assert self.card.sides == [8, 3, 4, 7]
        assert self.card.rotation_count == 3
        self.card.rotation()
        assert self.card.sides == [7, 8, 3, 4]
        assert self.card.rotation_count == 4

    def test_card_getLeft(self):
        assert self.card.getLeft() == 7
    
    def test_card_getUp(self):
        assert self.card.getUp() == 8

    def test_card_getRight(self):
        assert self.card.getRight() == 3

    def test_card_getDown(self):
        assert self.card.getDown() == 4
