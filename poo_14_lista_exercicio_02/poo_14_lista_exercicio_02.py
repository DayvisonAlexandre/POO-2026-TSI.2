# ============================================================
# - Lista de Exercícios 2 -
# - Encapsulamento e Exceções -
# ============================================================


# - Questão 1 -
# - Qual a diferença prática entre _saldo e __saldo? -
# - O que é name mangling? -

# - Resposta:
# _saldo indica que o atributo é considerado "protegido" por convenção.
# Ou seja, o Python não impede o acesso, mas o "_" indica que o atributo
# deve ser usado internamente pela classe ou por classes relacionadas.
#
# __saldo utiliza dois underscores no início. Nesse caso, o Python aplica
# o chamado name mangling, alterando internamente o nome do atributo para
# evitar colisões de nomes em subclasses.
#
# Por exemplo:
# __saldo
# passa internamente a ser algo semelhante a:
# _Conta__saldo


# - Questão 2 -
# - Sem executar: o que acontece em p.total = 10 se total é uma -
# - property sem setter? -

# - Resposta:
# Se "total" for uma property que possui apenas um getter e não possui
# setter, a tentativa de fazer:
#
# p.total = 10
#
# provoca um AttributeError.
#
# Isso acontece porque a propriedade permite a leitura de "total",
# mas não permite que seu valor seja alterado diretamente.


# - Questão 3 -
# - Por que validar no setter é melhor do que validar em cada ponto -
# - que usa o atributo? -

# - Resposta:
# Porque a validação fica centralizada em um único lugar.
#
# Assim, sempre que o valor do atributo for alterado, a mesma regra
# de validação será aplicada. Isso evita repetir a mesma validação em
# vários pontos do programa e diminui a possibilidade de alguma
# alteração esquecer de verificar uma regra importante.


# - Questão 4 -
# - Aponte o problema: except Exception: pass -

# - Resposta:
# O problema é que esse código captura praticamente qualquer exceção
# e simplesmente ignora o erro.
#
# Isso pode esconder problemas no programa e dificultar muito a
# identificação e correção de erros.
#
# Em vez de ignorar a exceção, o programa deve tratar especificamente
# os erros que são esperados e, quando necessário, informar o usuário
# sobre o problema.


# - Questão 5 -
# - O que herda quem escreve class MeuErro(Exception)? -

# - Resposta:
# A classe MeuErro herda da classe Exception.
#
# Portanto, MeuErro é uma exceção personalizada que pode ser lançada
# e capturada como uma exceção.
#
# Exemplo:
#
# class MeuErro(Exception):
#     pass
#
# Nesse caso, MeuErro herda os comportamentos da classe Exception.


# ============================================================
# - Questão 6 - Funcionário -
# ============================================================

SALARIO_MINIMO = 1621.00


class SalarioInvalidoError(Exception):
    pass


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if valor < SALARIO_MINIMO:
            raise SalarioInvalidoError(
                f"Salário inválido. O salário mínimo considerado é "
                f"R$ {SALARIO_MINIMO:.2f}."
            )

        self._salario = valor

    def aumentar(self, percentual):
        if percentual <= 0 or percentual > 30:
            raise ValueError(
                "O percentual deve ser maior que 0 e menor ou igual a 30."
            )

        self.salario = self.salario * (1 + percentual / 100)

    def __str__(self):
        return (
            f"Funcionário: {self.nome} | "
            f"Salário: R$ {self.salario:.2f}"
        )


# ============================================================
# - Questão 7 - Email -
# ============================================================

class EmailInvalidoError(Exception):
    pass


class Email:
    def __init__(self, endereco):
        self.endereco = endereco

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, valor):
        if "@" not in valor or "." not in valor:
            raise EmailInvalidoError(
                "E-mail inválido. O endereço deve conter '@' e '.'."
            )

        self._endereco = valor

    def __str__(self):
        return self.endereco


# ============================================================
# - Questões 6, 7 e 8 - Testes -
# ============================================================

def testar_funcionario_e_email():

    print("\n" + "=" * 55)
    print("TESTES - FUNCIONARIO")
    print("=" * 55)

    # Erro: salário abaixo do mínimo
    try:
        funcionario = Funcionario("João", 1000)

    except SalarioInvalidoError as erro:
        print("ERRO:", erro)

    # Erro: percentual maior que 30
    try:
        funcionario = Funcionario("Maria", 2000)
        funcionario.aumentar(50)

    except ValueError as erro:
        print("ERRO:", erro)

    # Funcionário válido
    funcionario = Funcionario("Carlos", 2000)

    print("\nFuncionário válido:")
    print(funcionario)

    funcionario.aumentar(10)

    print("Após aumento de 10%:")
    print(funcionario)

    print("\n" + "=" * 55)
    print("TESTES - EMAIL")
    print("=" * 55)

    # Erro: sem @
    try:
        email = Email("joao.gmail.com")

    except EmailInvalidoError as erro:
        print("ERRO:", erro)

    # Erro: sem .
    try:
        email = Email("joao@gmailcom")

    except EmailInvalidoError as erro:
        print("ERRO:", erro)

    # E-mail válido
    email = Email("carlos@gmail.com")

    print("\nE-mail válido:")
    print(email)


# ============================================================
# - Questão 9 - Conta Bancária -
# ============================================================

class ErroDeConta(Exception):
    """Exceção base para os erros da conta."""
    pass


class ValorInvalidoError(ErroDeConta):
    pass


class SaldoInsuficienteError(ErroDeConta):
    pass


class LimiteExcedidoError(ErroDeConta):
    pass


class ContaBancaria:
    LIMITE_SAQUE = 1000.00

    def __init__(self, saldo=0.0):

        if saldo < 0:
            raise ValorInvalidoError(
                "O saldo inicial não pode ser negativo."
            )

        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):

        if valor <= 0:
            raise ValorInvalidoError(
                "O valor do depósito deve ser maior que zero."
            )

        self._saldo += valor

    def sacar(self, valor):

        if valor <= 0:
            raise ValorInvalidoError(
                "O valor do saque deve ser maior que zero."
            )

        if valor > self.LIMITE_SAQUE:
            raise LimiteExcedidoError(
                "O limite de saque por operação é R$ 1.000,00."
            )

        if valor > self._saldo:
            raise SaldoInsuficienteError(
                "Saldo insuficiente para realizar o saque."
            )

        self._saldo -= valor


# ============================================================
# - Questão 10 - Caixa Eletrônico -
# ============================================================

def ler_valor():

    while True:

        try:
            valor = float(input("Digite o valor: R$ "))

            return valor

        except ValueError:
            print(
                "Entrada inválida. "
                "Digite apenas um número."
            )


def caixa_eletronico():

    conta = ContaBancaria()

    while True:

        print("\n" + "=" * 40)
        print("          CAIXA ELETRÔNICO")
        print("=" * 40)
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Saldo")
        print("4 - Sair")
        print("=" * 40)

        try:

            opcao = input(
                "Escolha uma opção: "
            ).strip()

            if opcao == "1":

                valor = ler_valor()

                conta.depositar(valor)

                print(
                    "\nDepósito realizado com sucesso!"
                )

                print(
                    f"Saldo atual: R$ {conta.saldo:.2f}"
                )

            elif opcao == "2":

                valor = ler_valor()

                conta.sacar(valor)

                print(
                    "\nSaque realizado com sucesso!"
                )

                print(
                    f"Saldo atual: R$ {conta.saldo:.2f}"
                )

            elif opcao == "3":

                print(
                    f"\nSaldo atual: "
                    f"R$ {conta.saldo:.2f}"
                )

            elif opcao == "4":

                print(
                    "\nPrograma encerrado."
                )

                break

            else:

                print(
                    "\nOpção inválida. "
                    "Escolha entre 1 e 4."
                )

        except ErroDeConta as erro:

            print(
                f"\nErro: {erro}"
            )

        except Exception as erro:

            print(
                f"\nErro inesperado: {erro}"
            )


# ============================================================
# - Programa Principal -
# ============================================================

if __name__ == "__main__":

    print("=" * 55)
    print("LISTA DE EXERCÍCIOS 2 - POO")
    print("ENCAPSULAMENTO E EXCEÇÕES")
    print("=" * 55)

    testar_funcionario_e_email()

    print("\n")
    print("=" * 55)
    print("CAIXA ELETRÔNICO")
    print("=" * 55)

    caixa_eletronico()
