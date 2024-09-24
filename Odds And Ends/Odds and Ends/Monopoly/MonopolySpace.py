from enum import StrEnum

class SpaceType(StrEnum):
    GO = "GO"
    Property = "Property"
    CommunityChest = "Community Chest"
    Tax = "Tax"
    Railroad = "Railroad"
    Chance = "Chance"
    Jail = "Jail"
    Utility = "Utility"
    FreeParking = "Free Parking"
    GoToJail = "Go To Jail"

class MonopolySpace:
    def __init__(self, spaceType: SpaceType, name: str):
        self.spaceType = spaceType
        self.name = name
        self.lands = 0

    def landOn(self):
        self.lands += 1
