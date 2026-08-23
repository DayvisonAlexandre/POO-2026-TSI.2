# - Exercício de Fixação 01 - Tuplas -

def elementos_pares(tupla):
    pares = tuple(numero for numero in tupla if numero % 2 == 0)
    return pares


numeros = (1, 2, 3, 4, 5)

resultado = elementos_pares(numeros)

print(resultado)

def ordenar_sem_repeticoes(tupla):
    resultado = tuple(sorted(set(tupla)))
    return resultado


nomes = ("banana", "maçã", "laranja", "banana", "uva")

resultado = ordenar_sem_repeticoes(nomes)

print(resultado)
