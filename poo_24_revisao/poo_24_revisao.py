class EntregaForaDeAreaError(Exception):
    pass


class DadosInvalidosError(Exception):
    pass

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from modelo.erros import (
    EntregaForaDeAreaError,
    DadosInvalidosError
)


# CLIENTE
@dataclass
class Cliente:
    nome: str


# PRATO
@dataclass
class Prato:
    nome: str
    preco: float

    def __post_init__(self):
        if not self.nome.strip():
            raise DadosInvalidosError("O nome do prato é obrigatório.")

        if self.preco < 0:
            raise DadosInvalidosError("O preço não pode ser negativo.")


# CARDAPIO
class Cardapio:

    def __init__(self):
        self.pratos = []

    def adicionar_prato(self, prato):
        if not isinstance(prato, Prato):
            raise TypeError("É necessário informar um objeto Prato.")

        self.pratos.append(prato)

    def listar_pratos(self):
        return self.pratos.copy()


# RESTAURANTE
class Restaurante:

    def __init__(self, nome):
        self.nome = nome

        # Composição: o restaurante cria seu próprio cardápio.
        self.cardapio = Cardapio()


# ENTREGADOR
class Entregador(ABC):

    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def taxa_entrega(self, distancia):
        pass


# ENTREGA DE BICICLETA
class DeBike(Entregador):

    LIMITE = 5
    TAXA_POR_KM = 2.00

    def taxa_entrega(self, distancia):

        if distancia < 0:
            raise DadosInvalidosError("Distância inválida.")

        if distancia > self.LIMITE:
            raise EntregaForaDeAreaError(
                "Entrega fora da área permitida para bicicleta!"
            )

        return distancia * self.TAXA_POR_KM


# ENTREGA DE MOTO
class DeMoto(Entregador):

    LIMITE = 20
    TAXA_POR_KM = 1.50

    def taxa_entrega(self, distancia):

        if distancia < 0:
            raise DadosInvalidosError("Distância inválida.")

        if distancia > self.LIMITE:
            raise EntregaForaDeAreaError(
                "Entrega fora da área permitida para motocicleta!"
            )

        return distancia * self.TAXA_POR_KM


# ITEM DO PEDIDO
@dataclass
class ItemPedido:
    prato: Prato
    quantidade: int

    def __post_init__(self):
        if self.quantidade <= 0:
            raise DadosInvalidosError(
                "A quantidade deve ser maior que zero."
            )

    def subtotal(self):
        return self.prato.preco * self.quantidade


# PEDIDO
@dataclass
class Pedido:
    cliente: Cliente
    entregador: Entregador
    distancia: float
    itens: list = field(default_factory=list)

    def __post_init__(self):
        if self.distancia < 0:
            raise DadosInvalidosError("Distância inválida.")

    def adicionar_item(self, prato, quantidade):
        item = ItemPedido(prato, quantidade)
        self.itens.append(item)

    def calcular_subtotal(self):
        return sum(item.subtotal() for item in self.itens)

from modelo.entidades import (
    Cliente,
    Prato,
    Cardapio,
    Restaurante,
    Entregador,
    DeBike,
    DeMoto,
    ItemPedido,
    Pedido
)

from modelo.servicos import ServicoDelivery

from modelo.erros import (
    EntregaForaDeAreaError,
    DadosInvalidosError
)

from modelo.entidades import Pedido


class ServicoDelivery:

    def calcular_total(self, pedido):

        if not isinstance(pedido, Pedido):
            raise TypeError("É necessário informar um Pedido.")

        subtotal = pedido.calcular_subtotal()

        taxa_entrega = pedido.entregador.taxa_entrega(
            pedido.distancia
        )

        return subtotal + taxa_entrega

    def exibir_pedido(self, pedido):

        total = self.calcular_total(pedido)

        print(f"Cliente: {pedido.cliente.nome}")
        print(f"Entregador: {pedido.entregador.nome}")

        print("\nItens do pedido:")

        for item in pedido.itens:
            print(
                f"{item.quantidade}x {item.prato.nome} "
                f"- R$ {item.subtotal():.2f}"
            )

        print(f"\nSubtotal: R$ {pedido.calcular_subtotal():.2f}")

        print(
            f"Taxa de entrega: "
            f"R$ {pedido.entregador.taxa_entrega(pedido.distancia):.2f}"
        )

        print(f"Total: R$ {total:.2f}")

from modelo import (
    Cliente,
    Prato,
    Restaurante,
    DeBike,
    DeMoto,
    Pedido,
    ServicoDelivery,
    EntregaForaDeAreaError,
    DadosInvalidosError
)


def main():

    # Criando restaurante
    restaurante = Restaurante("Restaurante Central")

    # Criando pratos
    hamburguer = Prato("Hamburguer", 25.00)
    pizza = Prato("Pizza", 40.00)
    refrigerante = Prato("Refrigerante", 8.00)

    # Adicionando pratos ao cardápio
    restaurante.cardapio.adicionar_prato(hamburguer)
    restaurante.cardapio.adicionar_prato(pizza)
    restaurante.cardapio.adicionar_prato(refrigerante)

    print("=" * 45)
    print(restaurante.nome)
    print("=" * 45)

    print("\nCARDÁPIO:")

    for prato in restaurante.cardapio.listar_pratos():
        print(f"{prato.nome} - R$ {prato.preco:.2f}")

    # Criando clientes
    cliente1 = Cliente("João")
    cliente2 = Cliente("Maria")

    # Criando entregadores
    entregador1 = DeBike("Carlos")
    entregador2 = DeMoto("Pedro")

    # Criando serviço
    servico = ServicoDelivery()

    # PRIMEIRO PEDIDO
    pedido1 = Pedido(
        cliente=cliente1,
        entregador=entregador1,
        distancia=3
    )

    pedido1.adicionar_item(hamburguer, 2)
    pedido1.adicionar_item(refrigerante, 1)

    # SEGUNDO PEDIDO
    pedido2 = Pedido(
        cliente=cliente2,
        entregador=entregador2,
        distancia=10
    )

    pedido2.adicionar_item(pizza, 1)
    pedido2.adicionar_item(refrigerante, 2)

    # Exibindo primeiro pedido
    print("\n" + "=" * 45)
    print("PRIMEIRO PEDIDO")
    print("=" * 45)

    try:
        servico.exibir_pedido(pedido1)

    except (EntregaForaDeAreaError, DadosInvalidosError) as erro:
        print("Erro:", erro)

    # Exibindo segundo pedido
    print("\n" + "=" * 45)
    print("SEGUNDO PEDIDO")
    print("=" * 45)

    try:
        servico.exibir_pedido(pedido2)

    except (EntregaForaDeAreaError, DadosInvalidosError) as erro:
        print("Erro:", erro)

    # Testando exceção de entrega fora da área
    print("\n" + "=" * 45)
    print("TESTE DE EXCEÇÃO")
    print("=" * 45)

    pedido3 = Pedido(
        cliente=cliente1,
        entregador=entregador1,
        distancia=8
    )

    pedido3.adicionar_item(hamburguer, 1)

    try:
        servico.exibir_pedido(pedido3)

    except EntregaForaDeAreaError as erro:
        print("Erro:", erro)

    except DadosInvalidosError as erro:
        print("Erro:", erro)


if __name__ == "__main__":
    main()
