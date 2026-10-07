# - Questão 01 -

class Produto:
    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco


class ItemPedido:
    def __init__(self, produto: Produto, quantidade: int) -> None:
        self.produto = produto
        self.quantidade = quantidade

    @property
    def subtotal(self) -> float:
        return self.produto.preco * self.quantidade


class Pedido:
    def __init__(self, cliente: "Cliente") -> None:
        self.cliente = cliente
        self._itens: list[ItemPedido] = []

    def adicionar(self, produto: Produto, quantidade: int) -> None:
        item = ItemPedido(produto, quantidade)
        self._itens.append(item)

    @property
    def total(self) -> float:
        return sum(item.subtotal for item in self._itens)


class Cliente:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self._pedidos: list[Pedido] = []

    def fazer_pedido(self) -> Pedido:
        pedido = Pedido(self)
        self._pedidos.append(pedido)
        return pedido

# - Justificativa -
# A relação entre Cliente e Pedido é uma associação, pois o cliente conhece seus pedidos e cada pedido referencia seu cliente.

# - Questão 02 -

class Pedido:
    def __init__(self, cliente: "Cliente") -> None:
        self.cliente = cliente
        self._itens: list[ItemPedido] = []

    def adicionar(self, produto: Produto, quantidade: int) -> None:
        item = ItemPedido(produto, quantidade)
        self._itens.append(item)

    @property
    def total(self) -> float:
        return sum(item.subtotal for item in self._itens)

    def __str__(self) -> str:
        linhas = [
            f"Cliente: {self.cliente.nome}",
            "Itens:"
        ]

        for item in self._itens:
            linhas.append(
                f"- {item.produto.nome} "
                f"x{item.quantidade} "
                f"= R$ {item.subtotal:.2f}"
            )

        linhas.append(f"Total: R$ {self.total:.2f}")

        return "\n".join(linhas)

cliente = Cliente("João")

produto1 = Produto("X-Burguer", 15.00)
produto2 = Produto("Refrigerante", 6.00)

pedido = cliente.fazer_pedido()

pedido.adicionar(produto1, 2)
pedido.adicionar(produto2, 1)

print(pedido)

# - Questão 03 -

class Apartamento:
    def __init__(self, numero: int) -> None:
        self.numero = numero

    def __str__(self) -> str:
        return f"Apartamento {self.numero}"


class Predio:
    def __init__(self, numero_andares: int) -> None:
        self.numero_andares = numero_andares
        self._apartamentos: list[Apartamento] = []

        for andar in range(1, numero_andares + 1):
            apartamento = Apartamento(andar)
            self._apartamentos.append(apartamento)

    def listar_apartamentos(self) -> None:
        for apartamento in self._apartamentos:
            print(apartamento)

predio = Predio(4)

predio.listar_apartamentos()

# - UML -

#┌──────────────────┐
#│      Predio      │
#├──────────────────┤
#│ - numero_andares │
#│ - apartamentos   │
#├──────────────────┤
#│ + listar_...()   │
#└────────┬─────────┘
#         ◆
#         │ 1
#         │
#         │ *
#┌────────▼─────────┐
#│   Apartamento    │
#├──────────────────┤
#│ - numero         │
#├──────────────────┤
#│ + __str__()      │
#└──────────────────┘

# - Questão 04 -

class Jogador:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.time = None

    def __str__(self) -> str:
        if self.time:
            return f"{self.nome} - {self.time.nome}"
        return f"{self.nome} - Sem time"


class Time:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self._jogadores: list[Jogador] = []

    def adicionar_jogador(self, jogador: Jogador) -> None:
        if jogador not in self._jogadores:
            self._jogadores.append(jogador)
            jogador.time = self

    def remover_jogador(self, jogador: Jogador) -> None:
        if jogador in self._jogadores:
            self._jogadores.remove(jogador)

            if jogador.time is self:
                jogador.time = None

    def listar_jogadores(self) -> None:
        for jogador in self._jogadores:
            print(jogador.nome)

jogador = Jogador("Carlos")

time1 = Time("Time A")
time2 = Time("Time B")

time1.adicionar_jogador(jogador)

print(jogador)

time1.remover_jogador(jogador)
time2.adicionar_jogador(jogador)

print(jogador)

# - UML -

#┌──────────────────┐
#│       Time       │
#├──────────────────┤
#│ - nome           │
#│ - jogadores      │
#├──────────────────┤
#│ + adicionar_...()│
#│ + remover_...()  │
#│ + listar_...()   │
#└────────◇─────────┘
#         │
#         │ 0..*
#         │
#┌────────▼─────────┐
#│     Jogador      │
#├──────────────────┤
#│ - nome           │
#│ - time           │
#├──────────────────┤
#│                  │
#└──────────────────┘

# - Questão 05 -

# - UML -

#                         ASSOCIAÇÃO
#                 ┌──────────────────────┐
#                 │                      │
#                 │       1        0..*  │
#┌────────────────▼─┐                ┌───▼───────────────┐
#│     Cliente      │                │      Pedido       │
#├──────────────────┤                ├───────────────────┤
#│ - nome: str      │                │ - cliente         │
#│ - pedidos        │                │ - itens           │
#├──────────────────┤                ├───────────────────┤
#│ + fazer_pedido() │                │ + adicionar()     │
#└──────────────────┘                │ + total: float    │
#                                    │ + __str__()       │
#                                    └────────◆───────────┘
#                                             │
#                                             │ 1
#                                             │
#                                             │ 0..*
#                                    ┌────────▼───────────┐
#                                    │    ItemPedido      │
#                                    ├────────────────────┤
#                                    │ - produto          │
#                                    │ - quantidade: int  │
#                                    ├────────────────────┤
#                                    │ + subtotal: float  │
#                                    └────────◇────────────┘
#                                             │
#                                             │ 1
#                                             │
#                                             │ 0..*
#                                    ┌────────▼───────────┐
#                                    │      Produto       │
#                                    ├────────────────────┤
#                                    │ - nome: str        │
#                                    │ - preco: float     │
#                                    └────────────────────┘
