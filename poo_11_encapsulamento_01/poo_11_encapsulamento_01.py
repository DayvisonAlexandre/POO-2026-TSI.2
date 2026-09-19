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


# - Exercício 02 — Cronometro -

class Cronometro:
    def __init__(self) -> None:
        self._segundos = 0

    def iniciar(self) -> None:
        self._segundos = 0

    def tique(self) -> None:
        self._segundos += 1

    def tempo_formatado(self) -> str:
        minutos = self._segundos // 60
        segundos = self._segundos % 60

        return f"{minutos:02d}:{segundos:02d}"


cronometro = Cronometro()
cronometro.iniciar()
cronometro.tique()
cronometro.tique()
cronometro.tique()

print(cronometro.tempo_formatado())


# - Exercício 03 — Name Mangling -

class ContaBancariaPrivada:
    def __init__(self) -> None:
        self.__saldo = 0.0


conta_privada = ContaBancariaPrivada()

print(conta_privada.__saldo)
