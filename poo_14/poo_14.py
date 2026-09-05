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


from irecebivel import IRecebivel


class Registro:

    def __init__(self):
        self.registro = []

    def adicionarItem(self, item: IRecebivel) -> None:
        self.registro.append(item)

    def listarItem(self) -> None:

        if not self.registro:
            print("Nenhum recebimento registrado.")
            return

        print("\n========== REGISTRO DE RECEBIMENTOS ==========")

        total_geral = 0.0

        for i, item in enumerate(self.registro, start=1):
            print(f"\n{i}. {item}")
            total_geral += item.totalizarRecebivel()

        print("\n----------------------------------------------")
        print(f"TOTAL GERAL RECEBIDO: R$ {total_geral:.2f}")
        print("==============================================")
