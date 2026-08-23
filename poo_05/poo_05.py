# - Exercício de Fixação 01 -

class No:
    def __init__(self, letra, prox):
        self.letra = letra
        self.prox = prox


# Lista original
lista = [
    No('e', 1),
    No('h', 2),
    No('b', 3),
    No('f', 4),
    No('a', 5),
    No('i', 6),
    No('c', 7),
    No('g', 8),
    No('d', -1)
]


# Ordem alfabética:
# a -> b -> c -> d -> e -> f -> g -> h -> i

lista[4].prox = 2   # a -> b
lista[2].prox = 6   # b -> c
lista[6].prox = 8   # c -> d
lista[8].prox = 0   # d -> e
lista[0].prox = 3   # e -> f
lista[3].prox = 7   # f -> g
lista[7].prox = 1   # g -> h
lista[1].prox = 5   # h -> i
lista[5].prox = -1  # i -> fim

l = 4

print("1 - Letras em ordem alfabética:")
while l != -1:
    print(lista[l].letra, end=' ')
    l = lista[l].prox

print()


lista[2].prox = 8

l = 4

print("\n2 - Removendo a letra 'c':")
while l != -1:
    print(lista[l].letra, end=' ')
    l = lista[l].prox

print()


lista[6].letra = 'j'


lista[2].prox = 6
lista[6].prox = 8

l = 4

print("\n3 - Substituindo 'c' por 'j':")
while l != -1:
    print(lista[l].letra, end=' ')
    l = lista[l].prox

print()
