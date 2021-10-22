from typing import List


class Card:
    """
    A class used to represent a card


    Attributes
    ----------
    sides : List[int]
        a list representing the witch color / part
    rotation_count: int
        a int representing the number of 90° rotation made by the piece

    Methods
    -------
    tostring()
        return sides in a string separed by ", "
    rotation()
        rotate the card by 90° and increment the rotation_count by one
    getLeft() - getUp() - getRight() - getDown()
        return the corresponding value for the corresponding side
    """

    def __init__(self, sides) -> None:
        self.sides: List[int] = sides
        self.rotation_count: int = 0

    def toString(self) -> str:
        return ", ".join(map(str, self.sides))

    def rotation(self) -> None:
        self.rotation_count = self.rotation_count + 1
        self.sides.insert(0, self.sides.pop(-1))

    def getLeft(self) -> int:
        return self.sides[0]

    def getUp(self) -> int:
        return self.sides[1]

    def getRight(self) -> int:
        return self.sides[2]

    def getDown(self) -> int:
        return self.sides[3]
