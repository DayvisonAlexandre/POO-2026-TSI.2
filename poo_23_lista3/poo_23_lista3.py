# - NÍVEL 1 — COMPREENSÃO -

# - Questão 01 -

# a) Pedido → Cliente: Associação, pois um pedido utiliza um cliente, mas não é responsável por criar ou controlar sua existência.

# b) Pedido → ItemPedido: Composição, pois um pedido é composto por seus itens. Os itens são criados e gerenciados pelo próprio pedido.

# c) Carrinho → Produto: Agregação, pois o carrinho possui produtos, mas eles existem independentemente dele.

# d) Pessoa → Interruptor: Associação, pois uma pessoa utiliza um interruptor, mas não é responsável por sua criação ou existência.

# - Questão 02 -

# Conclusão: Quando uma classe filha esquece de chamar super().__init__(), o construtor da classe pai não é executado. Consequentemente, os atributos inicializados exclusivamente pela classe pai, não serão criados automaticamente no objeto. devemos utilizar super().__init__(), para executar o construtor da classe pai, e inicializar corretamente os atributos herdados.

# Exemplo:

class Pessoa:
    def __init__(self, nome):
        self.nome = nome


class Aluno(Pessoa):
    def __init__(self, nome, matricula):
        self.matricula = matricula


aluno = Aluno("Carlos", 123)

print(aluno.matricula)

try:
    print(aluno.nome)
except AttributeError as erro:
    print("Erro:", erro)

# - Questão 03 -

class A:
    def ola(self):
        print("A")


class B(A):
    def ola(self):
        print("B")
        super().ola()


class C(A):
    def ola(self):
        print("C")
        super().ola()


class D(C, B):
    def ola(self):
        print("D")
        super().ola()


d = D()
d.ola()

print(D.mro())

# - Questão 04 -

# Conclusão: O uso de vários if isinstance(), para identificar cada tipo de animal, é considerado um antipadrão, porque dificulta a manutenção, e aumenta o acoplamento do código. com polimorfismo, cada classe implementa seu próprio comportamento, permitindo utilizar o mesmo método, sem precisar identificar o tipo do objeto.

# Exemplo (1°):

class Animal:
    pass


class Gato(Animal):
    pass


class Cachorro(Animal):
    pass


def emitir_som(animal):
    if isinstance(animal, Gato):
        print("Miau!")
    elif isinstance(animal, Cachorro):
        print("Au au!")

# Exemplo (2°):

class Animal:
    def emitir_som(self):
        pass


class Gato(Animal):
    def emitir_som(self):
        print("Miau!")


class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")


def emitir_som(animal):
    animal.emitir_som()


animais = [Gato(), Cachorro()]

for animal in animais:
    emitir_som(animal)

# - Questão 05 -

# Conclusão do pass: É um método que não possui implementação, mas não impede que a classe seja instanciada. Não executa nenhuma operação, e não obriga a implementação nas filhas.

# Exemplo:

class Animal:
    def emitir_som(self):
        pass


animal = Animal()
print("Objeto criado!")

# Conclusão do @abstractmethod: É um método abstrato, que estabelece uma obrigação para as classes filhas. Uma classe que possui métodos abstratos pendentes, não pode ser instanciada. Estabelece um contrato obrigatório, para as classes concretas.

# Exemplo:

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def emitir_som(self):
        pass

# - NÍVEL 2 — APLICAÇÃO: VEÍCULOS -

# - Questão 06 -

from abc import ABC, abstractmethod


class Veiculo(ABC):

    def __init__(self, placa, diaria):
        self.placa = placa
        self.diaria = diaria

    @abstractmethod
    def calcular_aluguel(self, dias):
        pass

    def descricao(self):
        return (
            f"Veículo: {self.__class__.__name__} | "
            f"Placa: {self.placa} | "
            f"Diária: R$ {self.diaria:.2f}"
        )


class Carro(Veiculo):

    def calcular_aluguel(self, dias):
        return self.diaria * dias


class Moto(Veiculo):

    def calcular_aluguel(self, dias):
        return self.diaria * dias * 0.80


class Caminhao(Veiculo):

    def calcular_aluguel(self, dias):
        return super().calcular_aluguel_base(dias) + 100

class Veiculo(ABC):

    def __init__(self, placa, diaria):
        self.placa = placa
        self.diaria = diaria

    def calcular_aluguel_base(self, dias):
        return self.diaria * dias

    @abstractmethod
    def calcular_aluguel(self, dias):
        pass

    def descricao(self):
        return (
            f"Veículo: {self.__class__.__name__} | "
            f"Placa: {self.placa} | "
            f"Diária: R$ {self.diaria:.2f}"
        )


class Carro(Veiculo):

    def calcular_aluguel(self, dias):
        return super().calcular_aluguel_base(dias)


class Moto(Veiculo):

    def calcular_aluguel(self, dias):
        return super().calcular_aluguel_base(dias) * 0.80


class Caminhao(Veiculo):

    def calcular_aluguel(self, dias):
        return super().calcular_aluguel_base(dias) + 100

# - Questão 07 -

class Locadora:

    def __init__(self):
        self.veiculos = []

    def cadastrar(self, veiculo):
        if not isinstance(veiculo, Veiculo):
            raise TypeError("É necessário cadastrar um veículo.")

        self.veiculos.append(veiculo)

    def faturamento_previsto(self, dias):
        total = 0

        for veiculo in self.veiculos:
            total += veiculo.calcular_aluguel(dias)

        return total

# TESTE das QUESTÕES 06 e 07:

locadora = Locadora()

carro = Carro("ABC-1234", 150)
moto = Moto("DEF-5678", 80)
caminhao = Caminhao("GHI-9012", 300)

locadora.cadastrar(carro)
locadora.cadastrar(moto)
locadora.cadastrar(caminhao)

for veiculo in locadora.veiculos:
    print(veiculo.descricao())
    print(f"Aluguel: R$ {veiculo.calcular_aluguel(2):.2f}")
    print()

print(
    f"Faturamento previsto: "
    f"R$ {locadora.faturamento_previsto(2):.2f}"
)

# - Questão 08 -

# Conclusão: Como Veiculo é uma classe abstrata, e possui o método abstrato calcular_aluguel(), não é permitido criar objetos diretamente dela. O TypeError comprova que a classe abstrata, não pode ser instanciada diretamente.

# Exemplo:

try:
    veiculo = Veiculo("ABC-1234", 150)

except TypeError as erro:
    print("Erro ao instanciar Veiculo:")
    print(erro)

# - NÍVEL 3 — INTEGRAÇÃO: DELIVERY -

# - Questão 09 -

class Prato:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Cardapio:

    def __init__(self):
        self.pratos = []

    def adicionar_prato(self, prato):
        if not isinstance(prato, Prato):
            raise TypeError("É necessário cadastrar um prato.")

        self.pratos.append(prato)

    def listar_pratos(self):
        for prato in self.pratos:
            print(f"{prato.nome} - R$ {prato.preco:.2f}")


class Restaurante:

    def __init__(self, nome):
        self.nome = nome
        self.cardapio = Cardapio()

# - Questão 10 -

from abc import ABC, abstractmethod


class EntregaForaDeAreaError(Exception):
    pass


class Entregador(ABC):

    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def taxa_entrega(self, distancia):
        pass


class DeBike(Entregador):

    LIMITE = 5

    def taxa_entrega(self, distancia):

        if distancia > self.LIMITE:
            raise EntregaForaDeAreaError(
                "Entrega fora da área permitida para bicicleta!"
            )

        return distancia * 2.00


class DeMoto(Entregador):

    LIMITE = 20

    def taxa_entrega(self, distancia):

        if distancia > self.LIMITE:
            raise EntregaForaDeAreaError(
                "Entrega fora da área permitida para motocicleta!"
            )

        return distancia * 1.50

# - Questão 11 -

class Cliente:

    def __init__(self, nome):
        self.nome = nome


class ItemPedido:

    def __init__(self, prato, quantidade):
        self.prato = prato
        self.quantidade = quantidade

    def subtotal(self):
        return self.prato.preco * self.quantidade


class Pedido:

    def __init__(self, cliente, entregador, distancia):
        self.cliente = cliente
        self.entregador = entregador
        self.distancia = distancia

        self.itens = []

    def adicionar_item(self, prato, quantidade):
        item = ItemPedido(prato, quantidade)
        self.itens.append(item)

    def calcular_total(self):

        total_pratos = sum(
            item.subtotal() for item in self.itens
        )

        taxa = self.entregador.taxa_entrega(
            self.distancia
        )

        return total_pratos + taxa

# - Questão 12 -

class EntregaForaDeAreaError(Exception):
    pass

entregador = DeBike("Carlos")

try:
    taxa = entregador.taxa_entrega(8)

except EntregaForaDeAreaError as erro:
    print("Erro:", erro)

# - Questão 13 -

restaurante = Restaurante("Restaurante Central")

hamburguer = Prato("Hamburguer", 25.00)
pizza = Prato("Pizza", 40.00)
refrigerante = Prato("Refrigerante", 8.00)

restaurante.cardapio.adicionar_prato(hamburguer)
restaurante.cardapio.adicionar_prato(pizza)
restaurante.cardapio.adicionar_prato(refrigerante)


cliente1 = Cliente("João")
cliente2 = Cliente("Maria")


entregador1 = DeBike("Carlos")
entregador2 = DeMoto("Pedro")


pedido1 = Pedido(cliente1, entregador1, 3)

pedido1.adicionar_item(hamburguer, 2)
pedido1.adicionar_item(refrigerante, 1)


pedido2 = Pedido(cliente2, entregador2, 10)

pedido2.adicionar_item(pizza, 1)
pedido2.adicionar_item(refrigerante, 2)


print("===== PRIMEIRO PEDIDO =====")
print("Cliente:", pedido1.cliente.nome)
print("Entregador:", pedido1.entregador.nome)

try:
    print(f"Total: R$ {pedido1.calcular_total():.2f}")

except EntregaForaDeAreaError as erro:
    print("Erro:", erro)


print("\n===== SEGUNDO PEDIDO =====")
print("Cliente:", pedido2.cliente.nome)
print("Entregador:", pedido2.entregador.nome)

try:
    print(f"Total: R$ {pedido2.calcular_total():.2f}")

except EntregaForaDeAreaError as erro:
    print("Erro:", erro)


print("\n===== TESTE DE EXCEÇÃO =====")

pedido3 = Pedido(cliente1, entregador1, 8)

pedido3.adicionar_item(hamburguer, 1)

try:
    print(f"Total: R$ {pedido3.calcular_total():.2f}")

except EntregaForaDeAreaError as erro:
    print("Erro:", erro)
