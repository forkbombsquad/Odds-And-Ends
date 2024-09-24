from Dice import Dice2d6

class RollResult:
    def __init__(self, dice: [int]):
        self.dice = dice
        self.total = self.getTotal()
        self.isDoubles = (dice[0] == dice[1])

    def getTotal(self) -> int:
        value = 0
        for die in self.dice:
            value += die
        return value


class MonopolyPlayer:
    def __init__(self, name: str):
        self.dice = Dice2d6()
        self.getOutOfJailFrees = 0
        self.turnsRemainingInJail = 0
        self.location = 0
        self.doublesCount = 0
        self.name = name

    def roll(self) -> RollResult:
        return RollResult(self.dice.roll())