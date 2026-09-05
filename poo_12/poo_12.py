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
