# - Exercício 01 — ContaBancaria -

class ContaBancaria:
    def __init__(self, titular: str) -> None:
        self.titular = titular
        self._saldo = 0.0

    def depositar(self, valor: float) -> None:
        self._saldo += valor

    def sacar(self, valor: float) -> bool:
        if valor > self._saldo:
            return False

        self._saldo -= valor
        return True

    def saldo(self) -> float:
        return self._saldo


conta = ContaBancaria("Maria")
conta.depositar(100.0)

print(conta.saldo())
print(conta.sacar(50.0))
print(conta.saldo())
print(conta.sacar(100.0))
print(conta.saldo())
