from motorista import MotoristaDAO
from motoristaCLI import MotoristaCLI

motorista = MotoristaDAO()
motoristaCLI = MotoristaCLI(motorista)
motoristaCLI.run()