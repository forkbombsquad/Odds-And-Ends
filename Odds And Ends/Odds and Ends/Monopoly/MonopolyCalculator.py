from Monopoly.MonopolyBoard import MonopolyBoard
from Monopoly.MonopolyPlayer import MonopolyPlayer, RollResult
from Monopoly.MonopolyCard import MonopolyCommunityChestCard, MonopolyChanceCard, ForcedMovementLocation, ChanceCardType, CommunityChestCardType
from Monopoly.MonopolySpace import SpaceType
import random

class MonopolySimulator:
    def __init__(self, maxTurns: int):
        self.maxTurns = maxTurns
        self.board = MonopolyBoard()

    def start(self):
        print("Starting...")
        currentTurn = 0
        while currentTurn < self.maxTurns:
            if currentTurn % 100000 == 0:
                print("Turn " + currentTurn.__str__() + " / " + self.maxTurns.__str__())
            for player in self.board.players:
                player.doublesCount = 0
                result = player.roll()
                if player.turnsRemainingInJail > 0:
                    if player.getOutOfJailFrees > 0:
                        player.getOutOfJailFrees = 0
                        player.turnsRemainingInJail = 0
                        self.normalPlayerTurn(player, result)
                    elif result.isDoubles:
                        player.turnsRemainingInJail = 0
                        self.normalPlayerTurn(player, result)
                    else:
                        player.turnsRemainingInJail -= 1
                else:
                    self.normalPlayerTurn(player, result)
            currentTurn += 1

    def getNewSpace(self, value) -> int:
        if value > self.board.maxSpaceNum:
            value = value - self.board.maxSpaceNum
        return value

    def normalPlayerTurn(self, player: MonopolyPlayer, result: RollResult):
        spaceIndex = self.getNewSpace(player.location + result.total)
        player.location = spaceIndex

        space = self.board.board[spaceIndex]
        space.lands += 1
        match space.spaceType:
            case SpaceType.Chance:
                card = self.drawChanceCard()
                match card.cardType:
                    case ChanceCardType.GetOutOfJailFree:
                        player.getOutOfJailFrees += 1
                    case ChanceCardType.ForcedMovement:
                        forcedMovementIndex = self.getForcedMovementLocation(player.location, card.forcedMovementLocation)
                        if forcedMovementIndex == self.board.jailIndex:
                            self.sendToJail(player)
                        else:
                            self.board.board[forcedMovementIndex].lands += 1
                            player.location = forcedMovementIndex
            case SpaceType.CommunityChest:
                card = self.drawCommunityChestCard()
                match card.cardType:
                    case CommunityChestCardType.GetOutOfJailFree:
                        player.getOutOfJailFrees += 1
                    case CommunityChestCardType.ForcedMovement:
                        forcedMovementIndex = self.getForcedMovementLocation(player.location, card.forcedMovementLocation)
                        if forcedMovementIndex == self.board.jailIndex:
                            self.sendToJail(player)
                        else:
                            self.board.board[forcedMovementIndex].lands += 1
                            player.location = forcedMovementIndex
            case SpaceType.GoToJail:
                self.sendToJail(player)
                return

        if result.isDoubles:
            player.doublesCount += 1
            if player.doublesCount < 3:
                result = player.roll()
                self.normalPlayerTurn(player, result)
            else:
                self.sendToJail(player)
                return

    def sendToJail(self, player: MonopolyPlayer):
        player.turnsRemainingInJail = 3
        player.location = self.board.jailIndex
        self.board.board[self.board.jailIndex].lands += 1

    def drawChanceCard(self) -> MonopolyChanceCard:
        if self.board.chanceCards.__len__() > 0:
            card = self.board.chanceCards.pop(0)
            self.board.chanceDiscards.append(card)
        else:
            self.board.chanceCards = self.board.chanceDiscards
            random.shuffle(self.board.chanceCards)
            card = self.board.chanceCards.pop(0)
        return card

    def drawCommunityChestCard(self) -> MonopolyCommunityChestCard:
        if self.board.communityChestCards.__len__() > 0:
            card = self.board.communityChestCards.pop(0)
            self.board.communityDiscards.append(card)
        else:
            self.board.communityChestCards = self.board.communityDiscards
            random.shuffle(self.board.communityChestCards)
            card = self.board.communityChestCards.pop(0)
        return card

    def getForcedMovementLocation(self, currentLocation: int, force: ForcedMovementLocation) -> int:
        match force:
            case ForcedMovementLocation.Go:
                return self.board.goIndex
            case ForcedMovementLocation.Jail:
                return self.board.jailIndex
            case ForcedMovementLocation.Reading:
                return self.board.readingRailroadIndex
            case ForcedMovementLocation.Boardwalk:
                return self.board.boardwalkIndex
            case ForcedMovementLocation.StCharles:
                return self.board.stCharlesIndex
            case ForcedMovementLocation.Illinois:
                return self.board.illinoisIndex
            case ForcedMovementLocation.Back3:
                newLoc = currentLocation - 3
                if newLoc >= 0:
                    return newLoc
                else:
                    return self.board.maxSpaceNum + (newLoc + 1)
            case ForcedMovementLocation.Utility:
                if self.board.utilityIndexes[0] > currentLocation:
                    return self.board.utilityIndexes[0]
                elif self.board.utilityIndexes[1] > currentLocation:
                    return self.board.utilityIndexes[1]
                else:
                    return self.board.utilityIndexes[0]
            case ForcedMovementLocation.Railroad:
                for rr in self.board.railroadIndexes:
                    if rr > currentLocation:
                        return rr
                return self.board.railroadIndexes[0]

    def printStats(self):
        self.board.board.sort(key=lambda x: x.lands, reverse=True)
        print("\n\n\n\n======================================\n\n\n\n")
        for property in self.board.board:
            print(property.name + " (" + property.lands.__str__() + ")")
