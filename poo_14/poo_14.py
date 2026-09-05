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


from irecebivel import IRecebivel


class Servico(IRecebivel):

    def __init__(self, descricao: str, horas_servico: float, valor_hora: float):
        self.descricao = descricao
        self.horas_servico = horas_servico
        self.valor_hora = valor_hora

    def totalizarRecebivel(self) -> float:
        return self.horas_servico * self.valor_hora

    def __str__(self) -> str:
        return (
            f"Serviço: {self.descricao} | "
            f"Horas: {self.horas_servico:.2f} | "
            f"Valor por hora: R$ {self.valor_hora:.2f} | "
            f"Total: R$ {self.totalizarRecebivel():.2f}"
        )
