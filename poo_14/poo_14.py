from abc import ABC, abstractmethod


class IRecebivel(ABC):

    @abstractmethod
    def totalizarRecebivel(self) -> float:
        pass


from irecebivel import IRecebivel


class ItemVenda(IRecebivel):

    def __init__(self, produto: str, quantidade: int, valor: float):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

    def totalizarRecebivel(self) -> float:
        return self.quantidade * self.valor

    def __str__(self) -> str:
        return (
            f"Produto: {self.produto} | "
            f"Quantidade: {self.quantidade} | "
            f"Valor unitário: R$ {self.valor:.2f} | "
            f"Total: R$ {self.totalizarRecebivel():.2f}"
        )
