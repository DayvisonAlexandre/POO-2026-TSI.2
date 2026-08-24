# - Questão - 01 -

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print("\nNotas digitadas:")
print(nota1)
print(nota2)
print(nota3)
print(nota4)

print(f"Média aritmética: {media:.2f}")

# - Questão - 02 -

anos = int(input("Digite a quantidade de anos: "))
meses = int(input("Digite a quantidade de meses: "))
dias = int(input("Digite a quantidade de dias: "))

total_dias = (anos * 365) + (meses * 30) + dias

print(f"Idade expressa em dias: {total_dias} dias")

# - Questão - 03 -

hora = int(input("Digite a hora: "))
minuto = int(input("Digite os minutos: "))

total_minutos = (hora * 60) + minuto

print(f"Minutos desde o início do dia: {total_minutos}")

# - Questão - 04 -

nome = input("Digite o nome completo do funcionário: ")
horas = float(input("Digite o número de horas trabalhadas no mês: "))
valor_hora = float(input("Digite o valor recebido por hora: R$ "))
filhos = int(input("Digite o número de filhos: "))

salario_bruto = horas * valor_hora
acrescimo = salario_bruto * (0.03 * filhos)
salario_final = salario_bruto + acrescimo

print("\n--- Dados do Funcionário ---")
print(f"Nome: {nome}")
print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Salário final: R$ {salario_final:.2f}")

# - Questão - 05 -

import math

largura = float(input("Digite a largura da sala em metros: "))
profundidade = float(input("Digite a profundidade da sala em metros: "))

area = largura * profundidade
potencia_necessaria = area * 18

quantidade_lampadas = math.ceil(potencia_necessaria / 60)

print(f"Área da sala: {area:.2f} m²")
print(f"Potência necessária: {potencia_necessaria:.2f} W")
print(f"Lâmpadas necessárias: {quantidade_lampadas}")

# - Questão - 06 -

brancos = int(input("Digite o número de votos brancos: "))
nulos = int(input("Digite o número de votos nulos: "))
validos = int(input("Digite o número de votos válidos: "))

total = brancos + nulos + validos

if total == 0:
    print("Não é possível calcular os percentuais.")
else:
    percentual_brancos = (brancos / total) * 100
    percentual_nulos = (nulos / total) * 100
    percentual_validos = (validos / total) * 100

    print(f"Total de eleitores: {total}")
    print(f"Votos brancos: {percentual_brancos:.2f}%")
    print(f"Votos nulos: {percentual_nulos:.2f}%")
    print(f"Votos válidos: {percentual_validos:.2f}%")

# - Questão - 07 -

fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9

print(f"Temperatura em Celsius: {celsius:.2f} °C")

# - Questão - 08 -

custo_fabrica = float(input("Digite o custo de fábrica do carro: R$ "))

distribuidor = custo_fabrica * 0.28
impostos = custo_fabrica * 0.45

custo_final = custo_fabrica + distribuidor + impostos

print(f"Custo final ao consumidor: R$ {custo_final:.2f}")

# - Questão - 09 -

numero = int(input("Digite um número entre 1 e 10: "))

if 1 <= numero <= 10:
    print("O número digitado está DENTRO da faixa solicitada.")
else:
    print("O número digitado está FORA da faixa solicitada.")

# - Questão - 10 -

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

if valor1 > valor2:
    print(f"O maior valor é: {valor1}")
elif valor2 > valor1:
    print(f"O maior valor é: {valor2}")
else:
    print("Os dois valores são iguais.")

# - Questão - 11 -

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

if valor1 > valor2:
    diferenca = valor1 - valor2
else:
    diferenca = valor2 - valor1

print(f"Diferença: {diferenca}")

# - Questão - 12 -

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

valores = [valor1, valor2, valor3]
valores.sort()

print("Valores em ordem crescente:")
print(valores[0], valores[1], valores[2])

# - Questão - 13 -

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

valores = [valor1, valor2, valor3]

opcao = input(
    "Digite C para ordem crescente ou D para ordem decrescente: "
).upper()

if opcao == "C":
    valores.sort()
    print("Ordem crescente:", valores)
elif opcao == "D":
    valores.sort(reverse=True)
    print("Ordem decrescente:", valores)
else:
    print("Opção inválida.")

# - Questão - 14 -

for numero in range(1, 101):
    print(numero)

# - Questão - 15 -

for numero in range(100, 0, -1):
    print(numero)

# - Questão - 16 -

inicio = int(input("Digite o primeiro valor: "))
fim = int(input("Digite o segundo valor: "))

if inicio > fim:
    inicio, fim = fim, inicio

soma = 0

print("Números do intervalo:")

for numero in range(inicio, fim + 1):
    print(numero)
    soma += numero

print(f"Somatório: {soma}")

# - Questão - 17 -

soma = 0

for i in range(10):
    numero = float(input(f"Digite o {i + 1}º número: "))
    soma += numero

print(f"Somatório: {soma}")

# - Questão - 18 -

soma = 0

for i in range(5):
    numero = float(input(f"Digite o {i + 1}º valor: "))

    if numero < 10:
        soma += numero

print(f"Somatório dos valores menores que 10: {soma}")

# - Questão - 19 -

soma = 0

for i in range(5):
    numero = float(input(f"Digite o {i + 1}º valor: "))

    if numero >= 10 and numero < 20:
        soma += numero

print(f"Somatório: {soma}")

# - Questão - 20 -

soma = 0

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º valor: "))

    if numero % 2 == 0:
        soma += numero

print(f"Somatório dos valores pares: {soma}")

# - Questão - 21 -

quantidade = int(input("Digite a quantidade de valores: "))

pares = 0

for i in range(quantidade):
    numero = int(input(f"Digite o {i + 1}º número: "))

    if numero % 2 == 0:
        pares += 1

print(f"Quantidade de números pares: {pares}")

# - Questão - 22 -

soma_impares = 0
soma_pares = 0

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))

    if i % 2 == 0:
        soma_impares += numero
    else:
        soma_pares += numero

print(f"Soma das posições ímpares: {soma_impares}")
print(f"Soma das posições pares: {soma_pares}")

if soma_impares > soma_pares:
    print("O somatório dos números ímpares é maior.")
elif soma_impares == soma_pares:
    print("Os somatórios são iguais.")
else:
    print("O somatório dos números pares é maior.")

# - Questão - 23 -

soma_pares = 0
soma_impares = 0

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))

    if numero % 2 == 0:
        soma_pares += numero
    else:
        soma_impares += numero

print(f"Soma dos números pares: {soma_pares}")
print(f"Soma dos números ímpares: {soma_impares}")

if soma_impares > soma_pares:
    print("O somatório dos números ímpares é maior.")
elif soma_impares == soma_pares:
    print("Os somatórios são iguais.")
else:
    print("O somatório dos números pares é maior.")

# - Questão - 24 -

quantidade = int(input("Digite o total de números a serem somados: "))

soma = 0
valores = []

for i in range(quantidade):
    numero = int(input(f"Digite o {i + 1}º número: "))
    valores.append(numero)
    soma += numero

expressao = "+".join(map(str, valores))

print(f"Saída no terminal: {expressao}={soma}")

# - Questão - 25 -

valores = []

for numero in range(1000, 3001):
    if numero % 7 == 0 and numero % 5 != 0:
        valores.append(str(numero))

print(";".join(valores))

# - Questão - 26 -

pares = 0
impares = 0

while True:
    numero = int(input("Digite um número negativo para encerrar: "))

    if numero < 0:
        break

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")

# - Questão - 27 -

valor = int(input("Digite um valor: "))

for numero in range(1, valor + 1):

    if numero % 3 == 0 and numero % 7 == 0:
        print("POW")
    elif numero % 3 == 0:
        print("PI")
    elif numero % 7 == 0:
        print("PA")
    else:
        print(numero)

# - Questão - 28 -

valores = []

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º valor: "))
    valores.append(numero)

quantidade_pares = 0

for numero in valores:
    if numero != 0 and numero % 2 == 0:
        quantidade_pares += 1

print(f"Quantidade de valores pares: {quantidade_pares}")

# - Questão - 29 -

notas = []

for i in range(10):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas.append(nota)

maior = max(notas)
menor = min(notas)
media = sum(notas) / len(notas)

print(f"Maior nota: {maior:.2f}")
print(f"Menor nota: {menor:.2f}")
print(f"Média das notas: {media:.2f}")

# - Questão - 30 -

vet1 = []
vet2 = []

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º valor: "))
    vet1.append(numero)

for i in range(5):
    numero = int(input(f"Digite o {i + 6}º valor: "))
    vet2.append(numero)

somaPAR = 0
somaIMPAR = 0

for numero in vet1 + vet2:
    if numero % 2 == 0:
        somaPAR += numero
    else:
        somaIMPAR += numero

print(f"vet1: {vet1}")
print(f"vet2: {vet2}")
print(f"somaPAR: {somaPAR}")
print(f"somaIMPAR: {somaIMPAR}")

# - Questão - 31 -

numero_atleta = 1

while True:
    print(f"\nAtleta {numero_atleta}")

    nome = input("Nome do atleta: ")

    if nome == "":
        break

    saltos = []

    for i in range(5):
        salto = float(input(f"{i + 1}º Salto: "))
        saltos.append(salto)

    media = sum(saltos) / 5

    print("\nResultado final:")
    print(f"Atleta: {nome}")
    print(
        "Saltos: "
        + " - ".join(f"{salto:.1f}" for salto in saltos)
    )
    print(f"Média dos saltos: {media:.2f} m")
    print("-------------------------------------------")

    numero_atleta += 1
