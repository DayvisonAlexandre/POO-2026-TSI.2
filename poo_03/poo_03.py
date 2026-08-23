# - Exercício de Fixação 01 -

numero = int(input("Digite um número inteiro: "))

if numero > 0:
    print("O número é positivo!")

# - Exercício de Fixação 02 -

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print("Média:", media)

if media >= 30 and media < 70:
    print("Você está em RECUPERAÇÃO!!!")

# - Exercício de Fixação 03 -

inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))
valor = int(input("Digite o valor a ser verificado: "))

if valor >= inicio and valor <= fim:
    print("O valor está dentro do intervalo.")
elif valor < inicio:
    print("O valor está abaixo do intervalo.")
else:
    print("O valor está acima do intervalo.")

# - Exercício de Fixação 04 -

print("=== MENOR CAMINHO ===")

ab = float(input("Digite a distância entre A e B: "))
ac = float(input("Digite a distância entre A e C: "))

bd = float(input("Digite a distância entre B e D: "))
be = float(input("Digite a distância entre B e E: "))

cf = float(input("Digite a distância entre C e F: "))
cg = float(input("Digite a distância entre C e G: "))

# Calcula as quatro possibilidades de caminho
caminho1 = ab + bd
caminho2 = ab + be
caminho3 = ac + cf
caminho4 = ac + cg

# Verifica qual é o menor caminho
if caminho1 <= caminho2 and caminho1 <= caminho3 and caminho1 <= caminho4:
    print("Caminho percorrido: A → B → D")
    print("Distância percorrida:", caminho1)

elif caminho2 <= caminho1 and caminho2 <= caminho3 and caminho2 <= caminho4:
    print("Caminho percorrido: A → B → E")
    print("Distância percorrida:", caminho2)

elif caminho3 <= caminho1 and caminho3 <= caminho2 and caminho3 <= caminho4:
    print("Caminho percorrido: A → C → F")
    print("Distância percorrida:", caminho3)

else:
    print("Caminho percorrido: A → C → G")
    print("Distância percorrida:", caminho4)
