import Constants
from CasinoDice.CasinoDiceSimulator import CasinoDiceSimulator
from Monopoly.MonopolyCalculator import MonopolySimulator

programMode = Constants.ProgramMode.MonopolyCalculator


def runCasinoDice():
    cs = CasinoDiceSimulator(maxRounds=1000000)
    cs.start()
    return

def runMonopolyCalculator():
    mc = MonopolySimulator(maxTurns=99999999)
    mc.start()
    mc.printStats()
    return

match programMode:
    case Constants.ProgramMode.CasinoDiceCalculator:
        runCasinoDice()
    case Constants.ProgramMode.MonopolyCalculator:
        runMonopolyCalculator()


