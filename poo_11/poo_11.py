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


from gato import Gato
from cachorro import Cachorro


# Testando o Gato
gato = Gato("Mimi", 4.5)

print("===== GATO =====")
gato.miar()

print("Está na árvore?", gato.estaNaArvore())

gato.subirNaArvore()
print("Está na árvore após subir?", gato.estaNaArvore())

gato.descerDaArvore()
print("Está na árvore após descer?", gato.estaNaArvore())


# Testando o Cachorro
cachorro = Cachorro("Rex", 12.5)

print("\n===== CACHORRO =====")
cachorro.latir()

print("Está cansado?", cachorro.estaCansado())

for i in range(6):
    cachorro.saltar()

print("Depois de 6 saltos:")
print("Está cansado?", cachorro.estaCansado())

cachorro.descansar()

print("Depois de descansar:")
print("Está cansado?", cachorro.estaCansado())
