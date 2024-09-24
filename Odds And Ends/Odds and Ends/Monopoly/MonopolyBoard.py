from Monopoly.MonopolySpace import MonopolySpace, SpaceType
from Monopoly.MonopolyCard import MonopolyChanceCard, MonopolyCommunityChestCard, ChanceCardType, CommunityChestCardType, ForcedMovementLocation
from Monopoly.MonopolyPlayer import MonopolyPlayer
import random

class MonopolyBoard:
    def __init__(self):
        self.board = [
            MonopolySpace(SpaceType.GO, "GO"),
            MonopolySpace(SpaceType.Property, "Mediterranean Ave"),
            MonopolySpace(SpaceType.CommunityChest, "Community Chest 1"),
            MonopolySpace(SpaceType.Property, "Baltic Ave"),
            MonopolySpace(SpaceType.Tax, "Income Tax"),
            MonopolySpace(SpaceType.Railroad, "Reading Railroad (1)"),
            MonopolySpace(SpaceType.Property, "Oriental Ave"),
            MonopolySpace(SpaceType.Chance, "Chance 1"),
            MonopolySpace(SpaceType.Property, "Vermont Ave"),
            MonopolySpace(SpaceType.Property, "Connecticut Ave"),
            MonopolySpace(SpaceType.Jail, "Jail"),
            MonopolySpace(SpaceType.Property, "St Charles Place"),
            MonopolySpace(SpaceType.Utility, "Electric Company"),
            MonopolySpace(SpaceType.Property, "States Ave"),
            MonopolySpace(SpaceType.Property, "Virgina Ave"),
            MonopolySpace(SpaceType.Railroad, "Pennsylvania Railroad (2)"),
            MonopolySpace(SpaceType.Property, "St James Place"),
            MonopolySpace(SpaceType.CommunityChest, "Community Chest 2"),
            MonopolySpace(SpaceType.Property, "Tennessee Ave"),
            MonopolySpace(SpaceType.Property, "New York Ave"),
            MonopolySpace(SpaceType.FreeParking, "Free Parking"),
            MonopolySpace(SpaceType.Property, "Kentucky Ave"),
            MonopolySpace(SpaceType.Chance, "Chance 2"),
            MonopolySpace(SpaceType.Property, "Indiana Ave"),
            MonopolySpace(SpaceType.Property, "Illinois Ave"),
            MonopolySpace(SpaceType.Railroad, "B&O Railroad (3)"),
            MonopolySpace(SpaceType.Property, "Atlantic Ave"),
            MonopolySpace(SpaceType.Property, "Ventnor Ave"),
            MonopolySpace(SpaceType.Utility, "Water Works"),
            MonopolySpace(SpaceType.Property, "Marvin Gardens"),
            MonopolySpace(SpaceType.GoToJail, "Go to Jail"),
            MonopolySpace(SpaceType.Property, "Pacific Ave"),
            MonopolySpace(SpaceType.Property, "North Carolina Ave"),
            MonopolySpace(SpaceType.CommunityChest, "Community Chest (3)"),
            MonopolySpace(SpaceType.Property, "Pennsylvania Ave"),
            MonopolySpace(SpaceType.Railroad, "Short Line (4)"),
            MonopolySpace(SpaceType.Chance, "Chance (3)"),
            MonopolySpace(SpaceType.Property, "Park Place"),
            MonopolySpace(SpaceType.Tax, "Luxury Tax"),
            MonopolySpace(SpaceType.Property, "Boardwalk")
        ]
        self.maxSpaceNum = 39
        self.goIndex = 0
        self.boardwalkIndex = 39
        self.illinoisIndex = 24
        self.stCharlesIndex = 11
        self.jailIndex = 10
        self.readingRailroadIndex = 5
        self.utilityIndexes = [12, 28]
        self.railroadIndexes = [5, 15, 25, 35]

        self.chanceCards = [
            MonopolyChanceCard(ChanceCardType.ForcedMovement, "Advance to Go", ForcedMovementLocation.Go),
            MonopolyChanceCard(ChanceCardType.ForcedMovement, "Advance to Illinois", ForcedMovementLocation.Illinois),
            MonopolyChanceCard(ChanceCardType.ForcedMovement, "Advance to St Charles Place", ForcedMovementLocation.StCharles),
            MonopolyChanceCard(ChanceCardType.ForcedMovement, "Advance to nearest Utility", ForcedMovementLocation.Utility),
            MonopolyChanceCard(ChanceCardType.ForcedMovement, "Advance to Nearest Railroad", ForcedMovementLocation.Railroad),
            MonopolyChanceCard(ChanceCardType.ForcedMovement, "Go Back 3 Spaces", ForcedMovementLocation.Back3),
            MonopolyChanceCard(ChanceCardType.ForcedMovement, "Advance to Jail", ForcedMovementLocation.Jail),
            MonopolyChanceCard(ChanceCardType.ForcedMovement, "Advance to Reading Railroad", ForcedMovementLocation.Reading),
            MonopolyChanceCard(ChanceCardType.ForcedMovement, "Advance to Boardwalk", ForcedMovementLocation.Boardwalk),
            MonopolyChanceCard(ChanceCardType.GetOutOfJailFree, "Get Out Of Jail Free"),
            MonopolyChanceCard(ChanceCardType.FineOrBonus, "Bank Dividend"),
            MonopolyChanceCard(ChanceCardType.FineOrBonus, "Property Repairs"),
            MonopolyChanceCard(ChanceCardType.FineOrBonus, "Poor Tax"),
            MonopolyChanceCard(ChanceCardType.FineOrBonus, "Chairman of Board"),
            MonopolyChanceCard(ChanceCardType.FineOrBonus, "Building Loan Matures")
        ]
        self.chanceDiscards = []

        random.shuffle(self.chanceCards)

        self.communityChestCards = [
            MonopolyCommunityChestCard(CommunityChestCardType.ForcedMovement, "Advance to Go", ForcedMovementLocation.Go),
            MonopolyCommunityChestCard(CommunityChestCardType.ForcedMovement, "Advance to Jail", ForcedMovementLocation.Jail),
            MonopolyCommunityChestCard(CommunityChestCardType.GetOutOfJailFree, "Get Out Of Jail Free"),
            MonopolyCommunityChestCard(CommunityChestCardType.FineOrBonus, "Bank Error"),
            MonopolyCommunityChestCard(CommunityChestCardType.FineOrBonus, "Doctor Fee"),
            MonopolyCommunityChestCard(CommunityChestCardType.FineOrBonus, "Opera"),
            MonopolyCommunityChestCard(CommunityChestCardType.FineOrBonus, "Holiday Fund"),
            MonopolyCommunityChestCard(CommunityChestCardType.FineOrBonus, "Income Tax Refund"),
            MonopolyCommunityChestCard(CommunityChestCardType.FineOrBonus, "Birthday"),
            MonopolyCommunityChestCard(CommunityChestCardType.FineOrBonus, "Life Insurance"),
            MonopolyCommunityChestCard(CommunityChestCardType.FineOrBonus, "Hospital Fees"),
            MonopolyCommunityChestCard(CommunityChestCardType.FineOrBonus, "School Fees"),
            MonopolyCommunityChestCard(CommunityChestCardType.FineOrBonus, "Consultancy Fee"),
            MonopolyCommunityChestCard(CommunityChestCardType.FineOrBonus, "Street Repairs"),
            MonopolyCommunityChestCard(CommunityChestCardType.FineOrBonus, "Beauty Contest"),
            MonopolyCommunityChestCard(CommunityChestCardType.FineOrBonus, "Inherit $100"),
            MonopolyCommunityChestCard(CommunityChestCardType.FineOrBonus, "Stonks")
        ]
        self.communityDiscards = []

        random.shuffle(self.communityChestCards)

        self.players = [
            MonopolyPlayer("Player 1"),
            MonopolyPlayer("Player 2"),
            MonopolyPlayer("Player 3"),
            MonopolyPlayer("Player 4")
        ]


