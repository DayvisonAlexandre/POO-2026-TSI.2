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


# - Exercício 04 — Aluno -

class Aluno:
    def __init__(self, nota: float) -> None:
        self.nota = nota

    @property
    def nota(self) -> float:
        return self._nota

    @nota.setter
    def nota(self, valor: float) -> None:
        if valor < 0 or valor > 10:
            raise ValueError("nota inválida")

        self._nota = valor


aluno = Aluno(8.5)

print(aluno.nota)

aluno.nota = 10.0

print(aluno.nota)


# - Exercício 05 — Retangulo -

class Retangulo:
    def __init__(self, base: float, altura: float) -> None:
        self.base = base
        self.altura = altura

    @property
    def base(self) -> float:
        return self._base

    @base.setter
    def base(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("base inválida")

        self._base = valor

    @property
    def altura(self) -> float:
        return self._altura

    @altura.setter
    def altura(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("altura inválida")

        self._altura = valor

    @property
    def area(self) -> float:
        return self._base * self._altura


retangulo = Retangulo(5.0, 3.0)

print(retangulo.base)
print(retangulo.altura)
print(retangulo.area)

retangulo.base = 10.0

print(retangulo.area)
