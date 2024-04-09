from Utils import rand, generateStandardDieSides

class Die:
    def __init__(self, sides: [int]):
        self.sides = sides

    def roll(self) -> int:
        rand(0, len(self.sides) - 1)


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