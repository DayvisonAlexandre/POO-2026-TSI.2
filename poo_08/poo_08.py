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
