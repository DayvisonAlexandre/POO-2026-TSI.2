from datetime import date


class QuantidadeInvalidaError(Exception):
    pass


class MedicamentoVencidoError(Exception):
    pass


class Medicamento:
    def __init__(
        self,
        nome: str,
        lote: str,
        validade: date,
        quantidade: int,
        valor: float,
    ):
        self.nome = nome
        self.lote = lote
        self.validade = validade
        self.quantidade = quantidade
        self.valor = valor

    @property
    def quantidade(self) -> int:
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade: int) -> None:
        if quantidade < 0:
            raise ValueError(

            )

        self._quantidade = quantidade

    @property
    def valor(self) -> float:
        return self._valor

    @valor.setter
    def valor(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError(

            )

        self._valor = valor

    @classmethod
    def de_registro(cls, registro: str):
        partes = registro.split(";")

        if len(partes) != 5:
            raise ValueError(

            )

        nome, lote, validade, quantidade, valor = partes

        try:
            validade = date.fromisoformat(validade)
        except ValueError as erro:
            raise ValueError(
            ) from erro

        try:
            quantidade = int(quantidade)
        except ValueError as erro:
            raise ValueError(
            ) from erro

        try:
            valor = float(valor)
        except ValueError as erro:
            raise ValueError(
            ) from erro

        return cls(
            nome,
            lote,
            validade,
            quantidade,
            valor
        )

    @staticmethod
    def dias_para_vencer(validade: date) -> int:
        
        return (validade - date.today()).days

    def __str__(self) -> str:
        
        return (
            f"{self.nome} ({self.lote}) - "
            f"{self.quantidade} un. - "
            f"val. {self.validade.strftime('%d/%m/%Y')}"
        )

    def __repr__(self) -> str:
        return (
            f"Medicamento("
            f"nome={self.nome!r}, "
            f"lote={self.lote!r}, "
            f"validade={self.validade!r}, "
            f"quantidade={self.quantidade!r}, "
            f"valor={self.valor!r}"
            f")"
        )

    def __eq__(self, outro) -> bool:
        if not isinstance(outro, Medicamento):
            return NotImplemented

        return (
            self.nome == outro.nome
            and self.lote == outro.lote
        )

    def __lt__(self, outro) -> bool:
        if not isinstance(outro, Medicamento):
            return NotImplemented

        return self.validade < outro.validade

    def dispensar(self, quantidade: int) -> None:
        if quantidade <= 0:
            raise QuantidadeInvalidaError(
                
            )

        if quantidade > self.quantidade:
            raise QuantidadeInvalidaError(
                
            )

        if self.validade < date.today():
            raise MedicamentoVencidoError(
                
            )

        self.quantidade -= quantidade

    def repor(self, quantidade: int) -> None:
        self.quantidade += quantidade


if __name__ == "__main__":
    m1 = Medicamento(
        "Dipirona 500mg",
        "L2026A",
        date(2026, 12, 31),
        100,
        12.50
    )

    m2 = Medicamento.de_registro(
        "Amoxicilina 500mg;L2026B;2026-10-15;40;18.90"
    )

    print(f"Dados de m1: {m1}")
    print(f"Dados de m2: {m2}")
    print(
        f"{Medicamento.dias_para_vencer(m2.validade)}"
    )

    print("\nDispensando 20 medicamentos de m1")
    m1.dispensar(20)
    print(f"Quantidade de m1: {m1.quantidade}")

    try:
        m2.dispensar(999)
    except QuantidadeInvalidaError as erro:
        print(f"Erro esperado: {erro}")

    vencido = Medicamento(
        "Soro Fisiológico",
        "L2025X",
        date(2025, 1, 10),
        10,
        5.00
    )

    try:
        vencido.dispensar(1)
    except MedicamentoVencidoError as erro:
        print(f"Erro esperado: {erro}")

    outro = Medicamento(
        "Dipirona 500mg",
        "L2026A",
        date(2026, 1, 1),
        0,
        1.00
    )

    print(f"m1 é igual a outro? {m1 == outro}")

    estoque = [m1, m2, vencido, outro]

    print("\nExibindo lista ordenada por data (mais antigos primeiro):")

    for lote in sorted(estoque):
        print(lote)

    try:
        m1.quantidade = -5
    except ValueError as erro:
        print(f"Erro esperado: {erro}")
