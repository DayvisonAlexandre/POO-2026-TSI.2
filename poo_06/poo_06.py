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

# - Exercício de Fixação 02 - Dicionários -

def pais_maior_populacao(paises):
    if not paises:
        return None

    maior_pais = max(paises, key=paises.get)

    return maior_pais


populacoes = {
    "Brasil": 211.8,
    "China": 1400.5,
    "Índia": 1366.4
}

resultado = pais_maior_populacao(populacoes)

print(resultado)

def alunos_aprovados(alunos):
    aprovados = {}

    for nome, notas in alunos.items():
        media = sum(notas) / len(notas)

        if media >= 7:
            aprovados[nome] = round(media, 2)

    return aprovados


alunos = {
    "Ana": [8.5, 9.0, 7.5],
    "Bruno": [6.0, 5.5, 4.0],
    "Carla": [7.0, 8.0, 9.0]
}

resultado = alunos_aprovados(alunos)

print(resultado)
