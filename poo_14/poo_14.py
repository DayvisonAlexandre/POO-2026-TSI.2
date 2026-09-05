from abc import ABC, abstractmethod


class IRecebivel(ABC):

    @abstractmethod
    def totalizarRecebivel(self) -> float:
        pass
