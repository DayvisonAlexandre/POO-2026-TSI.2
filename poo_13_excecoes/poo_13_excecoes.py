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
