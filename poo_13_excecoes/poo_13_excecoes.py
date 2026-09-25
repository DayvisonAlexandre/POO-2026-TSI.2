# ============================================================
# - Prática - Exceções: raise e Exceções Personalizadas -
# ============================================================


# ============================================================
# - 01. Conta Bancária -
# ============================================================

class ErroDeConta(Exception):
    """Classe base para erros relacionados à conta bancária."""
    pass


class SaldoInsuficienteError(ErroDeConta):
    """Exceção para tentativa de saque acima do saldo disponível."""
    pass


class ValorInvalidoError(ErroDeConta):
    """Exceção para valores inválidos de depósito ou saque."""
    pass


class ContaBancaria:
    def __init__(self, titular: str):
        self.titular = titular
        self._saldo = 0.0

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor: float):
        if valor <= 0:
            raise ValorInvalidoError(
                "O valor do depósito deve ser maior que zero."
            )

        self._saldo += valor

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValorInvalidoError(
                "O valor do saque deve ser maior que zero."
            )

        if valor > self._saldo:
            raise SaldoInsuficienteError(
                f"Saldo insuficiente. "
                f"Saldo disponível: R$ {self._saldo:.2f}; "
                f"valor solicitado: R$ {valor:.2f}"
            )

        self._saldo -= valor


# ============================================================
# - 02. Classe Aluno -
# ============================================================

class Aluno:
    def __init__(self, nome: str, nota: float):
        self.nome = nome
        self.nota = nota

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, valor):
        if valor < 0 or valor > 10:
            raise ValueError(
                "A nota deve estar entre 0 e 10."
            )

        self._nota = valor


# ============================================================
# - 03. Estacionamento -
# ============================================================

class EstacionamentoLotadoError(Exception):
    """Exceção lançada quando o estacionamento está cheio."""
    pass


class Estacionamento:
    def __init__(self, vagas: int):
        if vagas <= 0:
            raise ValueError(
                "A quantidade de vagas deve ser maior que zero."
            )

        self.vagas = vagas
        self.ocupadas = 0

    def entrar(self):
        if self.ocupadas >= self.vagas:
            raise EstacionamentoLotadoError(
                "Estacionamento lotado! Não há vagas disponíveis."
            )

        self.ocupadas += 1
        print(
            f"Veículo entrou. "
            f"Vagas ocupadas: {self.ocupadas}/{self.vagas}"
        )

    def sair(self):
        if self.ocupadas == 0:
            raise ValueError(
                "Não há veículos no estacionamento."
            )

        self.ocupadas -= 1
        print(
            f"Veículo saiu. "
            f"Vagas ocupadas: {self.ocupadas}/{self.vagas}"
        )


# ============================================================
# - Programa Principal -
# ============================================================

def main():

    print("=" * 60)
    print("1 - TESTE DA CONTA BANCÁRIA")
    print("=" * 60)

    conta = ContaBancaria("Maria")

    print(f"Titular: {conta.titular}")
    print(f"Saldo inicial: R$ {conta.saldo:.2f}")

    # Depósito válido
    try:
        conta.depositar(1000)
        print(f"Depósito realizado.")
        print(f"Saldo atual: R$ {conta.saldo:.2f}")

    except ValorInvalidoError as erro:
        print(f"Erro: {erro}")

    # Saque válido
    try:
        conta.sacar(300)
        print(f"Saque realizado.")
        print(f"Saldo atual: R$ {conta.saldo:.2f}")

    except SaldoInsuficienteError as erro:
        print(f"Operação negada: {erro}")

    except ValorInvalidoError as erro:
        print(f"Valor inválido: {erro}")

    # Saque maior que o saldo
    try:
        conta.sacar(1000)

    except SaldoInsuficienteError as erro:
        print(f"Operação negada: {erro}")

    except ValorInvalidoError as erro:
        print(f"Valor inválido: {erro}")

    # Depósito inválido
    try:
        conta.depositar(-50)

    except ValorInvalidoError as erro:
        print(f"Operação negada: {erro}")

    # Desafio: captura pela classe base
    print("\nTeste da exceção-base ErroDeConta:")

    try:
        conta.sacar(5000)

    except ErroDeConta as erro:
        print(f"Erro de conta capturado: {erro}")


    print("\n" + "=" * 60)
    print("2 - TESTE DA CLASSE ALUNO")
    print("=" * 60)

    try:
        aluno = Aluno("João", 8.5)

        print(f"Aluno: {aluno.nome}")
        print(f"Nota: {aluno.nota}")

        # Tentativa de nota inválida
        aluno.nota = 12

    except ValueError as erro:
        print(f"Erro ao cadastrar nota: {erro}")


    print("\n" + "=" * 60)
    print("3 - TESTE DO ESTACIONAMENTO")
    print("=" * 60)

    estacionamento = Estacionamento(2)

    try:
        estacionamento.entrar()
        estacionamento.entrar()
        estacionamento.entrar()

    except EstacionamentoLotadoError as erro:
        print(f"Entrada negada: {erro}")

    print("\nUm veículo irá sair:")

    estacionamento.sair()

    print("\nTentando entrar novamente:")

    try:
        estacionamento.entrar()

    except EstacionamentoLotadoError as erro:
        print(f"Entrada negada: {erro}")


    print("\n" + "=" * 60)
    print("FIM DOS TESTES")
    print("=" * 60)


if __name__ == "__main__":
    main()
