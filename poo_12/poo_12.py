from abc import ABC, abstractmethod
import math

# - Questão 01 -

# ============================================================
# CLASSE PONTO
# ============================================================

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    # Sobrecarga do operador +
    # Permite somar dois pontos.
    def __add__(self, outro):
        if not isinstance(outro, Ponto):
            return NotImplemented

        return Ponto(self.x + outro.x, self.y + outro.y)


# ============================================================
# CLASSE ABSTRATA FIGURA GEOMÉTRICA
# ============================================================

class FiguraGeometrica(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


# ============================================================
# CLASSE RETÂNGULO
# ============================================================

class Retangulo(FiguraGeometrica):

    def __init__(self, canto_superior_esquerdo, canto_inferior_direito):
        self.canto_superior_esquerdo = canto_superior_esquerdo
        self.canto_inferior_direito = canto_inferior_direito

        self.largura = abs(
            canto_inferior_direito.x - canto_superior_esquerdo.x
        )

        self.altura = abs(
            canto_superior_esquerdo.y - canto_inferior_direito.y
        )

    # Sobrescrita do método area()
    def area(self):
        return self.largura * self.altura

    # Sobrescrita do método perimetro()
    def perimetro(self):
        return 2 * (self.largura + self.altura)

    def __str__(self):
        return (
            f"Retângulo\n"
            f"  Canto superior esquerdo: "
            f"{self.canto_superior_esquerdo}\n"
            f"  Canto inferior direito: "
            f"{self.canto_inferior_direito}\n"
            f"  Largura: {self.largura}\n"
            f"  Altura: {self.altura}"
        )


# ============================================================
# CLASSE CÍRCULO
# ============================================================

class Circulo(FiguraGeometrica):

    def __init__(self, centro, raio):
        if raio <= 0:
            raise ValueError("O raio deve ser maior que zero.")

        self.centro = centro
        self.raio = raio

    # Sobrescrita do método area()
    def area(self):
        return math.pi * self.raio ** 2

    # Sobrescrita do método perimetro()
    def perimetro(self):
        return 2 * math.pi * self.raio

    def __str__(self):
        return (
            f"Círculo\n"
            f"  Centro: {self.centro}\n"
            f"  Raio: {self.raio}"
        )


# ============================================================
# FUNÇÃO PARA DEMONSTRAR POLIMORFISMO
# ============================================================

def apresentar_figura(figura):
    print(figura)
    print(f"  Área: {figura.area():.2f}")
    print(f"  Perímetro: {figura.perimetro():.2f}")


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():

    print("=" * 60)
    print("EXERCÍCIO 1 - FIGURAS GEOMÉTRICAS")
    print("=" * 60)

    # --------------------------------------------------------
    # Criando pontos
    # --------------------------------------------------------

    ponto1 = Ponto(2, 8)
    ponto2 = Ponto(8, 2)

    print("\n--- PONTOS ---")

    print(f"Ponto 1: {ponto1}")
    print(f"Ponto 2: {ponto2}")

    # --------------------------------------------------------
    # Sobrecarga do operador +
    # --------------------------------------------------------

    ponto3 = ponto1 + ponto2

    print("\n--- SOBRECARGA DO OPERADOR + ---")
    print(f"{ponto1} + {ponto2} = {ponto3}")

    # --------------------------------------------------------
    # Criando um retângulo
    # --------------------------------------------------------

    retangulo = Retangulo(
        Ponto(2, 8),
        Ponto(8, 2)
    )

    # --------------------------------------------------------
    # Criando um círculo
    # --------------------------------------------------------

    circulo = Circulo(
        Ponto(5, 5),
        4
    )

    # --------------------------------------------------------
    # Polimorfismo
    # --------------------------------------------------------

    figuras = [retangulo, circulo]

    print("\n--- POLIMORFISMO ---")

    for figura in figuras:
        apresentar_figura(figura)
        print("-" * 60)


if __name__ == "__main__":
    main()


#                    ┌──────────────────────────┐
#                    │     FiguraGeometrica     │
#                    │         <<ABC>>          │
#                    ├──────────────────────────┤
#                    │ + area()                 │
#                    │ + perimetro()            │
#                    └────────────┬─────────────┘
#                                 │
#                  ┌──────────────┴──────────────┐
#                  │                             │
#                  ▼                             ▼
#       ┌────────────────────┐       ┌────────────────────┐
#       │      Retangulo     │       │      Circulo       │
#       ├────────────────────┤       ├────────────────────┤
#       │ - cantoSupEsq      │       │ - centro : Ponto   │
#       │ - cantoInfDir      │       │ - raio             │
#       │ - largura          │       ├────────────────────┤
#       │ - altura            │       │ + area()           │
#       ├────────────────────┤       │ + perimetro()      │
#       │ + area()           │       └─────────┬──────────┘
#       │ + perimetro()      │                 │
#       └─────────┬──────────┘                 │
#                 │                            │
#                 │         ┌──────────────────┘
#                 │         │
#                 ▼         ▼
#             ┌──────────────────┐
#             │      Ponto       │
#             ├──────────────────┤
#             │ - x              │
#             │ - y              │
#             ├──────────────────┤
#             │ + __add__()      │
#             └──────────────────┘

# - Questão 02 -

# ============================================================
# CLASSE BASE ANIMAL
# ============================================================

class Animal:

    def __init__(self, nome, idade, custo_alimentacao):
        if idade < 0:
            raise ValueError("A idade não pode ser negativa.")

        if custo_alimentacao < 0:
            raise ValueError("O custo de alimentação não pode ser negativo.")

        self.nome = nome
        self.idade = idade
        self.custo_alimentacao = custo_alimentacao

    def movimentar(self):
        print(f"{self.nome} está se movimentando.")

    def emitir_som(self):
        print(f"{self.nome} emitiu um som.")

    def alimentar(self):
        print(
            f"{self.nome} possui custo de alimentação de "
            f"R$ {self.custo_alimentacao:.2f} por dia."
        )

    def apresentar(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(
            f"Custo de alimentação: "
            f"R$ {self.custo_alimentacao:.2f} por dia"
        )


# ============================================================
# CLASSE LEÃO
# ============================================================

class Leao(Animal):

    def movimentar(self):
        print(f"{self.nome} está caminhando e correndo.")

    def emitir_som(self):
        print(f"{self.nome} está rugindo.")

    def alimentar(self):
        print(
            f"{self.nome} se alimenta principalmente de carne. "
            f"Custo diário: R$ {self.custo_alimentacao:.2f}"
        )


# ============================================================
# CLASSE ELEFANTE
# ============================================================

class Elefante(Animal):

    def movimentar(self):
        print(f"{self.nome} está caminhando lentamente.")

    def emitir_som(self):
        print(f"{self.nome} está emitindo um som característico.")

    def alimentar(self):
        print(
            f"{self.nome} se alimenta de vegetais, frutas e folhas. "
            f"Custo diário: R$ {self.custo_alimentacao:.2f}"
        )


# ============================================================
# CLASSE MACACO
# ============================================================

class Macaco(Animal):

    def movimentar(self):
        print(f"{self.nome} está pulando e subindo nas árvores.")

    def emitir_som(self):
        print(f"{self.nome} está emitindo sons característicos de macaco.")

    def alimentar(self):
        print(
            f"{self.nome} se alimenta de frutas, sementes e vegetais. "
            f"Custo diário: R$ {self.custo_alimentacao:.2f}"
        )


# ============================================================
# CLASSE PINGUIM
# ============================================================

class Pinguim(Animal):

    def movimentar(self):
        print(f"{self.nome} está caminhando e nadando.")

    def emitir_som(self):
        print(f"{self.nome} está emitindo sons característicos.")

    def alimentar(self):
        print(
            f"{self.nome} se alimenta principalmente de peixes. "
            f"Custo diário: R$ {self.custo_alimentacao:.2f}"
        )


# ============================================================
# CLASSE ZOOLÓGICO
# ============================================================

class Zoologico:

    def __init__(self, nome):
        self.nome = nome
        self.animais = []

    def adicionar_animal(self, animal):
        if not isinstance(animal, Animal):
            raise TypeError(
                "Somente objetos da classe Animal podem "
                "ser adicionados ao zoológico."
            )

        self.animais.append(animal)

    def listar_animais(self):
        print(f"\nZoológico: {self.nome}")
        print(f"Quantidade de animais: {len(self.animais)}")

        for animal in self.animais:
            print("-" * 50)
            animal.apresentar()

    def movimentar_animais(self):
        print("\n--- MOVIMENTAÇÃO DOS ANIMAIS ---")

        for animal in self.animais:
            animal.movimentar()

    def sons_dos_animais(self):
        print("\n--- SONS DOS ANIMAIS ---")

        for animal in self.animais:
            animal.emitir_som()

    def alimentar_animais(self):
        print("\n--- ALIMENTAÇÃO DOS ANIMAIS ---")

        for animal in self.animais:
            animal.alimentar()

    def custo_total_diario(self):
        total = 0

        for animal in self.animais:
            total += animal.custo_alimentacao

        return total


#                       ┌───────────────────────┐
#                       │        Animal         │
#                       ├───────────────────────┤
#                       │ - nome                │
#                       │ - idade               │
#                       │ - custo_alimentacao   │
#                       ├───────────────────────┤
#                       │ + movimentar()        │
#                       │ + emitir_som()        │
#                       │ + alimentar()         │
#                       │ + apresentar()        │
#                       └───────────┬───────────┘
#                                   │
#              ┌────────────────────┼────────────────────┐
#              │                    │                    │
#              ▼                    ▼                    ▼
#       ┌─────────────┐      ┌─────────────┐      ┌─────────────┐
#       │    Leao     │      │  Elefante   │      │   Macaco    │
#       ├─────────────┤      ├─────────────┤      ├─────────────┤
#       │ +movimentar │      │ +movimentar │      │ +movimentar │
#       │ +emitir_som │      │ +emitir_som │      │ +emitir_som │
#       │ +alimentar  │      │ +alimentar  │      │ +alimentar  │
#       └─────────────┘      └─────────────┘      └─────────────┘
#                                   │
#                                   │
#                                   ▼
#                            ┌─────────────┐
#                            │  Pinguim    │
#                            ├─────────────┤
#                            │+movimentar  │
#                            │+emitir_som  │
#                            │+alimentar   │
#                            └─────────────┘
#
#
#                       ┌───────────────────────┐
#                       │      Zoologico        │
#                       ├───────────────────────┤
#                       │ - nome                │
#                       │ - animais             │
#                       ├───────────────────────┤
#                       │ + adicionar_animal()  │
#                       │ + listar_animais()    │
#                       │ + movimentar_animais()│
#                       │ + sons_dos_animais()  │
#                       │ + alimentar_animais() │
#                       │ + custo_total_diario()│
#                       └───────────┬───────────┘
#                                   │
#                                   │ possui vários
#                                   ▼
#                                Animal


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():

    print("=" * 60)
    print("EXERCÍCIO 2 - SISTEMA DE ZOOLÓGICO")
    print("=" * 60)

    # Criando o zoológico
    zoologico = Zoologico("Zoológico Municipal")

    # Criando os animais
    leao = Leao("Simba", 8, 150.00)
    elefante = Elefante("Dumbo", 15, 200.00)
    macaco = Macaco("Chico", 5, 80.00)
    pinguim = Pinguim("Pingo", 4, 60.00)

    # Adicionando os animais ao zoológico
    zoologico.adicionar_animal(leao)
    zoologico.adicionar_animal(elefante)
    zoologico.adicionar_animal(macaco)
    zoologico.adicionar_animal(pinguim)

    # Listagem
    zoologico.listar_animais()

    # Polimorfismo: cada animal se movimenta de forma diferente
    zoologico.movimentar_animais()

    # Polimorfismo: cada animal emite um som diferente
    zoologico.sons_dos_animais()

    # Polimorfismo: alimentação diferente
    zoologico.alimentar_animais()

    # Custo total
    total = zoologico.custo_total_diario()

    print("\n--- CUSTO TOTAL ---")
    print(f"Custo total de alimentação por dia: R$ {total:.2f}")


if __name__ == "__main__":
    main()
