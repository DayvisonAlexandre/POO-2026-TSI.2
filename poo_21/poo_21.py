from abc import ABC, abstractmethod
import math


# ============================================================
# - QUESTÃO 01 - FORMAS GEOMÉTRICAS -
# ============================================================

class Forma(ABC):

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimetro(self) -> float:
        pass

    def descreva(self) -> str:
        return (
            f"{type(self).__name__}: "
            f"área = {self.area():.2f}, "
            f"perímetro = {self.perimetro():.2f}"
        )


class Retangulo(Forma):

    def __init__(self, largura: float, altura: float) -> None:
        if largura <= 0 or altura <= 0:
            raise ValueError("Largura e altura devem ser positivas.")

        self.largura = largura
        self.altura = altura

    def area(self) -> float:
        return self.largura * self.altura

    def perimetro(self) -> float:
        return 2 * (self.largura + self.altura)


class Circulo(Forma):

    def __init__(self, raio: float) -> None:
        if raio <= 0:
            raise ValueError("O raio deve ser positivo.")

        self.raio = raio

    def area(self) -> float:
        return math.pi * self.raio ** 2

    def perimetro(self) -> float:
        return 2 * math.pi * self.raio


# ============================================================
# - QUESTÃO 02 - TESTES DAS CLASSES ABSTRATAS -
# ============================================================

class FormaIncompleta(Forma):
    pass


def testar_formas_abstratas() -> None:
    print("\n--- QUESTÃO 2: TESTES DE ABSTRAÇÃO ---")

    try:
        Forma()
    except TypeError as erro:
        print(f"Forma() gerou TypeError: {erro}")

    try:
        FormaIncompleta()
    except TypeError as erro:
        print(f"FormaIncompleta() gerou TypeError: {erro}")


# ============================================================
# - QUESTÃO 03 - CONTAS BANCÁRIAS -
# ============================================================

class ContaBancaria(ABC):

    def __init__(self, saldo_inicial: float = 0.0) -> None:
        if saldo_inicial < 0:
            raise ValueError("O saldo inicial não pode ser negativo.")

        self._saldo = saldo_inicial

    @property
    def saldo(self) -> float:
        return self._saldo

    @abstractmethod
    def sacar(self, valor: float) -> bool:
        pass


class ContaCorrente(ContaBancaria):

    def __init__(
        self,
        saldo_inicial: float = 0.0,
        limite: float = 0.0
    ) -> None:
        if limite < 0:
            raise ValueError("O limite não pode ser negativo.")

        super().__init__(saldo_inicial)
        self._limite = limite

    @property
    def limite(self) -> float:
        return self._limite

    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            return False

        if valor > self._saldo + self._limite:
            return False

        self._saldo -= valor
        return True


class ContaPoupanca(ContaBancaria):

    def sacar(self, valor: float) -> bool:
        if valor <= 0 or valor > self._saldo:
            return False

        self._saldo -= valor
        return True


# ============================================================
# - QUESTÃO 04 - SISTEMA DE PAGAMENTO -
# ============================================================

class Pagavel(ABC):

    @abstractmethod
    def processar(self, valor: float) -> str:
        pass


class Pix(Pagavel):

    def processar(self, valor: float) -> str:
        if valor <= 0:
            raise ValueError("O valor deve ser positivo.")

        return f"Pagamento de R$ {valor:.2f} processado via Pix."


class Cartao(Pagavel):

    def processar(self, valor: float) -> str:
        if valor <= 0:
            raise ValueError("O valor deve ser positivo.")

        return f"Pagamento de R$ {valor:.2f} processado via cartão."


class Boleto(Pagavel):

    def processar(self, valor: float) -> str:
        if valor <= 0:
            raise ValueError("O valor deve ser positivo.")

        return f"Boleto de R$ {valor:.2f} gerado com sucesso."


def processar_pagamentos(
    pagamentos: list[Pagavel],
    valor: float
) -> None:
    for pagamento in pagamentos:
        print(pagamento.processar(valor))


# ============================================================
# - EXECUÇÃO E TESTES -
# ============================================================

def main() -> None:

    print("=== QUESTÃO 1: FORMAS GEOMÉTRICAS ===")

    formas: list[Forma] = [
        Retangulo(5, 3),
        Circulo(2)
    ]

    for forma in formas:
        print(forma.descreva())

    testar_formas_abstratas()

    print("\n--- QUESTÃO 3: CONTAS BANCÁRIAS ---")

    corrente = ContaCorrente(saldo_inicial=100, limite=50)
    poupanca = ContaPoupanca(saldo_inicial=100)

    print(f"Saldo inicial da conta corrente: R$ {corrente.saldo:.2f}")
    print(f"Saque de R$ 120,00 na conta corrente: "
          f"{'aprovado' if corrente.sacar(120) else 'recusado'}")
    print(f"Saldo após o saque: R$ {corrente.saldo:.2f}")

    print(f"\nSaque de R$ 120,00 na poupança: "
          f"{'aprovado' if poupanca.sacar(120) else 'recusado'}")
    print(f"Saldo da poupança: R$ {poupanca.saldo:.2f}")

    print("\n--- QUESTÃO 4: SISTEMA DE PAGAMENTO ---")

    pagamentos: list[Pagavel] = [
        Pix(),
        Cartao(),
        Boleto()
    ]

    processar_pagamentos(pagamentos, 150.00)


if __name__ == "__main__":
    main()
