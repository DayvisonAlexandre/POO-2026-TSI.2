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
