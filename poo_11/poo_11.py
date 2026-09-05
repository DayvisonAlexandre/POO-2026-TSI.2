class Animal:
    def __init__(self, nome, peso):
        self._nome = nome
        self._peso = peso
        self._posicao = 0

    def moverse(self):
        pass


from animal import Animal


class Cachorro(Animal):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)
        self._qtdSaltos = 0

    def latir(self):
        print("Au Au!")

    def saltar(self):
        self._qtdSaltos += 1

    def descansar(self):
        self._qtdSaltos -= 1

    def estaCansado(self):
        return self._qtdSaltos > 5
