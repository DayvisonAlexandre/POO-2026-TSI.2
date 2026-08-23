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
