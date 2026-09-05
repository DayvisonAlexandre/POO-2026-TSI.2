import math


# ============================================================
# CLASSE POINT
# ============================================================

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# ============================================================
# CLASSE RECTANGLE
# ============================================================

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def corners(self):
        """
        Retorna os quatro cantos do retângulo.
        """
        return [
            Point(self.x, self.y),
            Point(self.x + self.width, self.y),
            Point(self.x, self.y + self.height),
            Point(self.x + self.width, self.y + self.height)
        ]


# - Questão 01 -


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


print("=" * 60)
print("QUESTÃO 1 - DEFINIÇÃO DA CLASSE CIRCLE")
print("=" * 60)

centro_teste = Point(0, 0)
circulo_teste = Circle(centro_teste, 10)

print("Classe Circle criada com sucesso!")
print(f"Centro: ({circulo_teste.center.x}, {circulo_teste.center.y})")
print(f"Raio: {circulo_teste.radius}")


# - Questão 02 -


print("\n" + "=" * 60)
print("QUESTÃO 2 - INSTÂNCIA DO CÍRCULO")
print("=" * 60)

centro = Point(150, 100)
circulo = Circle(centro, 75)

print("Objeto Circle criado com sucesso!")
print(f"Centro: ({circulo.center.x}, {circulo.center.y})")
print(f"Raio: {circulo.radius}")


# - Questão 03 -


def point_in_circle(circle, point):
    """
    Retorna True se o ponto estiver dentro ou no limite
    do círculo.
    """

    distancia_quadrada = (
        (point.x - circle.center.x) ** 2
        + (point.y - circle.center.y) ** 2
    )

    raio_quadrado = circle.radius ** 2

    return distancia_quadrada <= raio_quadrado


print("\n" + "=" * 60)
print("QUESTÃO 3 - POINT_IN_CIRCLE")
print("=" * 60)

ponto_dentro = Point(150, 120)
ponto_limite = Point(225, 100)
ponto_fora = Point(250, 100)

print(
    f"Ponto (150, 120) está dentro/no limite? "
    f"{point_in_circle(circulo, ponto_dentro)}"
)

print(
    f"Ponto (225, 100) está dentro/no limite? "
    f"{point_in_circle(circulo, ponto_limite)}"
)

print(
    f"Ponto (250, 100) está dentro/no limite? "
    f"{point_in_circle(circulo, ponto_fora)}"
)
