from enum import StrEnum

class ChanceCardType(StrEnum):
    ForcedMovement = "Forced Movement"
    FineOrBonus = "Fine or Bonus"
    GetOutOfJailFree = "Get Out Of Jail Free"

class CommunityChestCardType(StrEnum):
    ForcedMovement = "Forced Movement"
    FineOrBonus = "Fine or Bonus"
    GetOutOfJailFree = "Get Out Of Jail Free"

class ForcedMovementLocation(StrEnum):
    Go = "GO"
    Boardwalk = "Boardwalk"
    Illinois = "Illinois"
    StCharles = "St Charles Place"
    Jail = "Jail"
    Reading = "Reading Railroad"
    Utility = "Nearest Utility"
    Railroad = "Nearest Railroad"
    Back3 = "Go Back 3 Spaces"

class MonopolyChanceCard:
    def __init__(self, cardType: ChanceCardType, name: str, forcedMovementLocation: ForcedMovementLocation = None):
        self.cardType = cardType
        self.name = name
        self.lands = 0
        self.forcedMovementLocation = forcedMovementLocation

class MonopolyCommunityChestCard:
    def __init__(self, cardType: CommunityChestCardType, name: str, forcedMovementLocation: ForcedMovementLocation = None):
        self.cardType = cardType
        self.name = name
        self.lands = 0
        self.forcedMovementLocation = forcedMovementLocation
