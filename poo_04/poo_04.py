# - Exercício de Fixação 01 - Questão 1 -

numero = int(input("Digite um número inteiro: "))

fatorial = 1

for i in range(1, numero + 1):
    fatorial = fatorial * i

print("O fatorial de", numero, "é:", fatorial)

# - Exercício de Fixação 01 - Questão 2 -

quantidade = int(input("Quantos usuários irão responder? "))

while quantidade <= 0:
    print("A quantidade deve ser maior que zero.")
    quantidade = int(input("Quantos usuários irão responder? "))

insatisfeito = 0
satisfeito = 0
nao_responder = 0

for i in range(quantidade):
    print("\n1 - INSATISFEITO")
    print("2 - SATISFEITO")
    print("3 - NÃO QUERO RESPONDER")

    resposta = int(input("Digite a opção: "))

    while resposta < 1 or resposta > 3:
        print("Opção inválida!")
        resposta = int(input("Digite a opção novamente: "))

    if resposta == 1:
        insatisfeito += 1
    elif resposta == 2:
        satisfeito += 1
    else:
        nao_responder += 1

percentual_insatisfeito = insatisfeito * 100 / quantidade
percentual_satisfeito = satisfeito * 100 / quantidade
percentual_nao_responder = nao_responder * 100 / quantidade

print("\n=== RESULTADO DA PESQUISA ===")
print("INSATISFEITO:", percentual_insatisfeito, "%")
print("SATISFEITO:", percentual_satisfeito, "%")
print("NÃO QUERO RESPONDER:", percentual_nao_responder, "%")

# - Exercício de Fixação 02 - Questão 1 -

temperatura = float(input("Digite a temperatura atual: "))

while temperatura >= 0:

    if temperatura < 15:
        print("Aqui não é o RN")

    elif temperatura <= 25:
        print("Pense num frio")

    elif temperatura <= 30:
        print("Temperatura normal e super agradável")

    elif temperatura <= 35:
        print("Tá quente pra danado")

    else:
        print("Calor da muléstia!")

    temperatura = float(input("\nDigite outra temperatura: "))
