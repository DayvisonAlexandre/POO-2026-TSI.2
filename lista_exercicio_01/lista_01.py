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
