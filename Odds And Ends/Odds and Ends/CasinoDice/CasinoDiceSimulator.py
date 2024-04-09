from Utils import rand


class CasinoDiceSimulator:
    def __init__(self, maxRounds: int):
        self.maxRounds = maxRounds
        self.p1score = 0
        self.p2score = 0
        self.p3score = 0
        self.p4score = 0
        self.p5score = 0
        self.pdice = 0
        self.pscore = 0
        self.slots = [0, 0, 0, 0, 0, 0]
        self.bust = False

    def runRound(self, dieCutoff: int) -> int:
        self.pdice = 6
        self.bust = False
        self.pscore = 0
        count = 0
        while self.pdice > dieCutoff and not self.bust:
            self.slots = [0, 0, 0, 0, 0, 0]
            diceThisRound = 0
            side = 1
            twoCount = 0
            uniqueCount = 0
            ones = 0
            fives = 0
            count = 0
            while count < self.pdice:
                self.slots[rand(1, 6) - 1] += 1
                count += 1

            diceThisRound = 0
            twoCount = 0
            uniqueCount = 0
            ones = 0
            fives = 0

            # Triples
            side = 1
            while side <= 6:
                if self.slots[side - 1] >= 3:
                    self.pscore += (side * 100)
                    if side == 1:
                        self.pscore += 900
                    diceThisRound += 3
                    self.slots[side - 1] -= 3
                    if self.slots[side - 1] == 3:
                        self.pscore += (side * 100)
                        if side == 1:
                            self.pscore += 900
                        diceThisRound += 3
                        self.slots[side - 1] -= 3
                side += 1

            # 3 Pair
            for num in self.slots:
                if num == 2:
                    twoCount += 1
            if twoCount == 3:
                self.pscore += 1000
                diceThisRound = 6
                self.slots = [0, 0, 0, 0, 0, 0]

            # Straight
            for num in self.slots:
                if num == 1:
                    uniqueCount += 1
            if uniqueCount == 6:
                self.pscore += 1000
                diceThisRound = 6
                self.slots = [0, 0, 0, 0, 0, 0]

            # Ones or Fives
            ones = self.slots[0]
            if ones > 0:
                self.pscore += 100 * ones
                diceThisRound += ones
                self.slots[0] = 0

            fives = self.slots[4]
            if fives > 0:
                self.pscore += 100 * ones
                diceThisRound += ones
                self.slots[0] = 0

            if diceThisRound == 0:
                self.bust = True
                self.pscore = 0
            else:
                self.pdice -= diceThisRound
                if self.pdice == 0:
                    self.pdice = 6

        # print(f"+{self.pscore}")
        return self.pscore

    def start(self) -> int:
        currentRound = 0
        while currentRound < self.maxRounds:
            self.p1score += self.runRound(dieCutoff=1)
            self.p2score += self.runRound(dieCutoff=2)
            self.p3score += self.runRound(dieCutoff=3)
            self.p4score += self.runRound(dieCutoff=4)
            self.p5score += self.runRound(dieCutoff=5)
            currentRound += 1
            # print(f"Round {currentRound}")
            if currentRound % 10000 == 0:
                print(f"Round: {currentRound}")

        print(f"\n\nSTOPPING AFTER KEEPING...\n"
              f"1 Dice: {self.p1score} (avg/rnd: {int(self.p1score / self.maxRounds)})\n"
              f"2 Dice: {self.p2score} (avg/rnd: {int(self.p2score / self.maxRounds)})\n"
              f"3 Dice: {self.p3score} (avg/rnd: {int(self.p3score / self.maxRounds)})\n"
              f"4 Dice: {self.p4score} (avg/rnd: {int(self.p4score / self.maxRounds)})\n"
              f"5 Dice: {self.p5score} (avg/rnd: {int(self.p5score / self.maxRounds)})")
