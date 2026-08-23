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
