from random import randint

from .card import Card


class Generator:
    class card:
        HEAD = [1, 2, 3, 4]
        BODY = [5, 6, 7, 8]
        HEAD_BODY = HEAD + BODY

        def new(self):
            """
            Generate a new card with randomly selected sides
            """

            # First we can randomly select the first two side
            return self.conditional_generator(
                [self.HEAD_BODY[randint(0, len(self.HEAD_BODY) - 1)] for _ in range(2)]
            )

        def conditional_generator(self, card):
            # for the last 2 sides, we need to check that there no more than two self.HEAD/self.BODY,
            # and if yes we should add the opposite (self.HEAD/self.BODY),
            # If there equality one self.HEAD and one self.BODY, we check the type of the last side, and we
            # add the same type of side, since self.BODY and self.HEAD should be next other two by two
            for _ in range(2):
                if sum(card.count(x) for x in set(self.HEAD)) >= 2:
                    card.append(self.BODY[randint(0, len(self.BODY) - 1)])
                elif sum(card.count(x) for x in set(self.BODY)) >= 2:
                    card.append(self.HEAD[randint(0, len(self.HEAD) - 1)])
                elif card[-1] in self.HEAD:
                    card.append(self.HEAD[randint(0, len(self.HEAD) - 1)])
                else:
                    card.append(self.BODY[randint(0, len(self.BODY) - 1)])
            return card

    class board:
        def new():
            """
            Generate a game board using randomly generated card
            """
            return [Card(Generator.card().new()) for _ in range(9)]
