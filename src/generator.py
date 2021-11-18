from random import randint

from .card import Card


class Generator:
    class card:
        HEAD = [1, 2, 3, 4]
        BODY = [5, 6, 7, 8]

        def new(self):
            """
            Generate a new card with randomly selected sides
            """
            card = []
            head = [1, 2, 3, 4]
            body = [5, 6, 7, 8]
            head_body = head + body

            # First we can randomly select the first two side
            for _ in range(2):
                rand = randint(0, len(head_body) - 1)
                card.append(head_body[rand])
                # since we can't reuse same slide we need to remove head_body[rand]
                head_body.pop(rand)
                if rand > (len(head) - 1):
                    body.pop(rand - len(head))
                else:
                    head.pop(rand)
            return self.conditional_generator(card, head, body)

        def conditional_generator(self, card, head, body):
            # for the last 2 sides, we need to check that there no more than two HEAD/BODY,
            # and if yes we should add the opposite (HEAD/BODY),
            # If there equality one HEAD and one BODY, we check the type of the last side, and we
            # add the same type of side, since BODY and HEAD should be next other two by two
            # Since we coulnd't have 2 times the same part, we need to remove part allready put

            for _ in range(2):
                if sum(card.count(x) for x in set(self.HEAD)) >= 2:
                    rand = randint(0, len(body) - 1)
                    card.append(body[rand])
                    body.pop(rand)
                elif sum(card.count(x) for x in set(self.BODY)) >= 2:
                    rand = randint(0, len(head) - 1)
                    card.append(head[rand])
                    head.pop(rand)

                elif card[-1] in self.HEAD:
                    rand = randint(0, len(head) - 1)
                    card.append(head[rand])
                    head.pop(rand)
                else:
                    rand = randint(0, len(body) - 1)
                    card.append(body[rand])
                    body.pop(rand)
            return card

    class board:
        def new():
            """
            Generate a game board using randomly generated card
            """
            return [Card(Generator.card().new()) for _ in range(9)]
