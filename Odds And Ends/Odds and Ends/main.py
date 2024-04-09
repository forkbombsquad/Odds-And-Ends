import Constants
from CasinoDice.CasinoDiceSimulator import CasinoDiceSimulator

programMode = Constants.ProgramMode.CasinoDiceCalculator


def runCasinoDice():
    cs = CasinoDiceSimulator(maxRounds=1000000)
    cs.start()
    return

match programMode:
    case Constants.ProgramMode.CasinoDiceCalculator:
        runCasinoDice()


