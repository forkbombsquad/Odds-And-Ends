from Utils import rand, generateStandardDieSides

class Die:
    def __init__(self, sides: [int]):
        self.sides = sides

    def roll(self) -> int:
        return rand(0, len(self.sides) - 1) + 1


class Dice:

    def __init__(self, dice: [Die]):
        self.dice = dice

    def roll(self) -> [int]:
        total = []
        for die in self.dice:
            total.append(die.roll())
        return total

class D4(Die):
    def __init__(self):
        super().__init__(generateStandardDieSides(4))

class D6(Die):
    def __init__(self):
        super().__init__(generateStandardDieSides(6))

class D8(Die):
    def __init__(self):
        super().__init__(generateStandardDieSides(8))

class D10(Die):
    def __init__(self):
        super().__init__(generateStandardDieSides(10))

class D12(Die):
    def __init__(self):
        super().__init__(generateStandardDieSides(12))

class D20(Die):
    def __init__(self):
        super().__init__(generateStandardDieSides(20))

class Dice2d6(Dice):
    def __init__(self):
        super().__init__([D6(), D6()])