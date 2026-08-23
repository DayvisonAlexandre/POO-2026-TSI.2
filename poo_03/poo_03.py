# - Exercício de Fixação 01 -

numero = int(input("Digite um número inteiro: "))

if numero > 0:
    print("O número é positivo!")

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
