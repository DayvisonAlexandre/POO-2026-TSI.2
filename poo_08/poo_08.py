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


# - Questão 04 -


def rect_in_circle(circle, rectangle):
    """
    Retorna True se todos os quatro cantos do retângulo
    estiverem dentro ou no limite do círculo.
    """

    for corner in rectangle.corners():
        if not point_in_circle(circle, corner):
            return False

    return True


print("\n" + "=" * 60)
print("QUESTÃO 4 - RECT_IN_CIRCLE")
print("=" * 60)

retangulo_dentro = Rectangle(120, 70, 60, 40)
retangulo_fora = Rectangle(200, 80, 80, 40)

print("Retângulo 1:")
for i, corner in enumerate(retangulo_dentro.corners(), start=1):
    print(f"  Canto {i}: ({corner.x}, {corner.y})")

print(
    f"Retângulo 1 está totalmente dentro/no limite? "
    f"{rect_in_circle(circulo, retangulo_dentro)}"
)

print("\nRetângulo 2:")
for i, corner in enumerate(retangulo_fora.corners(), start=1):
    print(f"  Canto {i}: ({corner.x}, {corner.y})")

print(
    f"Retângulo 2 está totalmente dentro/no limite? "
    f"{rect_in_circle(circulo, retangulo_fora)}"
)


# - Questão 05 -


def ponto_mais_proximo_retangulo(rectangle, point):
    """
    Encontra o ponto do retângulo que está mais próximo
    de um determinado ponto.
    """

    x_min = rectangle.x
    x_max = rectangle.x + rectangle.width

    y_min = rectangle.y
    y_max = rectangle.y + rectangle.height

    x_proximo = max(x_min, min(point.x, x_max))
    y_proximo = max(y_min, min(point.y, y_max))

    return Point(x_proximo, y_proximo)


def rect_circle_overlap(circle, rectangle):
    """
    Versão mais desafiadora da questão 5.

    Retorna True se alguma parte do retângulo estiver
    dentro ou no limite do círculo.

    A função verifica o ponto do retângulo mais próximo
    do centro do círculo.
    """

    ponto_proximo = ponto_mais_proximo_retangulo(
        rectangle,
        circle.center
    )

    return point_in_circle(circle, ponto_proximo)


print("\n" + "=" * 60)
print("QUESTÃO 5 - RECT_CIRCLE_OVERLAP")
print("=" * 60)

retangulo_sem_sobreposicao = Rectangle(250, 150, 50, 50)

retangulo_sobreposto = Rectangle(210, 90, 50, 30)

retangulo_com_canto_dentro = Rectangle(210, 140, 30, 30)

print("Retângulo 3:")
for i, corner in enumerate(
    retangulo_sem_sobreposicao.corners(),
    start=1
):
    print(f"  Canto {i}: ({corner.x}, {corner.y})")

print(
    f"Existe alguma parte do Retângulo 3 dentro/no limite "
    f"do círculo? "
    f"{rect_circle_overlap(circulo, retangulo_sem_sobreposicao)}"
)


print("\nRetângulo 4:")
for i, corner in enumerate(
    retangulo_sobreposto.corners(),
    start=1
):
    print(f"  Canto {i}: ({corner.x}, {corner.y})")

print(
    f"Existe alguma parte do Retângulo 4 dentro/no limite "
    f"do círculo? "
    f"{rect_circle_overlap(circulo, retangulo_sobreposto)}"
)


print("\nRetângulo 5:")
for i, corner in enumerate(
    retangulo_com_canto_dentro.corners(),
    start=1
):
    print(f"  Canto {i}: ({corner.x}, {corner.y})")

print(
    f"Existe alguma parte do Retângulo 5 dentro/no limite "
    f"do círculo? "
    f"{rect_circle_overlap(circulo, retangulo_com_canto_dentro)}"
)
