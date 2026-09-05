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


from animal import Animal


class Gato(Animal):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)
        self._naArvore = False

    def miar(self):
        print("Miau!")

    def subirNaArvore(self):
        self._naArvore = True

    def descerDaArvore(self):
        self._naArvore = False

    def estaNaArvore(self):
        return self._naArvore
