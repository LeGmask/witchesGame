from src.generator import Generator


class TestGenerator:
    generator_card = Generator.card()

    HEAD = [1, 2, 3, 4]
    BODY = [5, 6, 7, 8]
    HEAD_BODY = HEAD + BODY

    def check_card_condition_position(self, sides):
        """
        Check if two card of each type are next each other
        """
        if sides[0] in self.BODY:
            return sides[1] in self.BODY or sides[-1] in self.BODY
        elif sides[0] in self.HEAD:
            return sides[1] in self.HEAD or sides[-1] in self.HEAD

    def check_card_condition_count(self, sides):
        """
        Check if there exactly two card for each type : body and head
        """
        return (
            sum(sides.count(x) for x in set(self.HEAD)) == 2
            and sum(sides.count(x) for x in set(self.BODY)) == 2
        )

    def test_card_conditional_generator(self):
        # case when allready two head:
        sides = self.generator_card.conditional_generator([1, 2])
        assert self.check_card_condition_count(sides)
        assert self.check_card_condition_position(sides)

        # case when allready two body:
        sides = self.generator_card.conditional_generator([5, 7])
        assert self.check_card_condition_count(sides)
        assert self.check_card_condition_position(sides)

        # case when allready body equal head:
        sides = self.generator_card.conditional_generator([1, 7])
        assert self.check_card_condition_count(sides)
        assert self.check_card_condition_position(sides)

    def test_card_new(self):
        sides = self.generator_card.new()
        assert self.check_card_condition_count(sides)
        assert self.check_card_condition_position(sides)

    def test_board_new(self):
        board = Generator.board.new()
        for card in board:
            sides = card.sides
            assert self.check_card_condition_count(sides)
            assert self.check_card_condition_position(sides)
