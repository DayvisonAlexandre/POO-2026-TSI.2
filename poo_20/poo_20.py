# - Questão 01 -

class Animal:
    def __init__(self, nome: str) -> None:
        self._nome = nome
        self._posicao = 0

    def mover_se(self) -> None:
        self._posicao += 1


class Gato(Animal):
    def mover_se(self) -> None:
        print(f"{self._nome} caminhando...")
        self._posicao += 1


class Peixe(Animal):
    def mover_se(self) -> None:
        print(f"{self._nome} nadando...")
        self._posicao += 1


class Passaro(Animal):
    def mover_se(self) -> None:
        print(f"{self._nome} voando...")
        self._posicao += 1


class Cobra(Animal):
    def mover_se(self) -> None:
        print(f"{self._nome} rastejando...")
        self._posicao += 1


def mover_todos(animais: list[Animal]) -> None:
    for animal in animais:
        animal.mover_se()


zoologico = [
    Gato("Tom"),
    Peixe("Nemo"),
    Passaro("Blu"),
    Cobra("Sss"),
]

mover_todos(zoologico)

# - Questão 02 -

import math


class Retangulo:
    def __init__(self, largura: float, altura: float) -> None:
        self.largura = largura
        self.altura = altura

    def area(self) -> float:
        return self.largura * self.altura


class Circulo:
    def __init__(self, raio: float) -> None:
        self.raio = raio

    def area(self) -> float:
        return math.pi * self.raio ** 2


class Triangulo:
    def __init__(self, base: float, altura: float) -> None:
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return (self.base * self.altura) / 2


def area_total(formas) -> float:
    total = 0.0

    for forma in formas:
        total += forma.area()

    return total


formas = [
    Retangulo(5, 3),
    Circulo(2),
    Triangulo(4, 6),
]

for forma in formas:
    print(f"Área: {forma.area():.2f}")

print(f"Área total: {area_total(formas):.2f}")

# - Questão 03 -

class TocadorMP3:
    def tocar(self) -> None:
        print("Tocador MP3: reproduzindo música.")


class Radio:
    def tocar(self) -> None:
        print("Rádio: reproduzindo transmissão.")


dispositivos = [
    TocadorMP3(),
    Radio(),
]

for dispositivo in dispositivos:
    dispositivo.tocar()

# - Questão 04 -

class Tela:
    def escrever(self, mensagem: str) -> None:
        print(mensagem)


class ArquivoFake:
    def __init__(self) -> None:
        self.conteudo = []

    def escrever(self, mensagem: str) -> None:
        self.conteudo.append(mensagem)


class RelatorioPedidos:
    def __init__(self, saida) -> None:
        self.saida = saida

    def gerar(self) -> None:
        self.saida.escrever("Relatório de pedidos")
        self.saida.escrever("Pedido 001 - R$ 100,00")
        self.saida.escrever("Pedido 002 - R$ 50,00")
        self.saida.escrever("Total: R$ 150,00")


tela = Tela()
relatorio_tela = RelatorioPedidos(tela)

print("=== Relatório na tela ===")
relatorio_tela.gerar()


arquivo = ArquivoFake()
relatorio_arquivo = RelatorioPedidos(arquivo)

print("\n=== Conteúdo do ArquivoFake ===")
relatorio_arquivo.gerar()

for linha in arquivo.conteudo:
    print(linha)

# - Questão 05 -

def area_da_forma(forma) -> float:
    if isinstance(forma, Retangulo):
        return forma.largura * forma.altura
    elif isinstance(forma, Circulo):
        return math.pi * forma.raio ** 2
    elif isinstance(forma, Triangulo):
        return (forma.base * forma.altura) / 2
    else:
        raise TypeError("Forma não reconhecida")

def area_da_forma(forma) -> float:
    return forma.area()
