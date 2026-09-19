# - E08 - Lista de Exercícios 1 -
# - Fundamentos de Programação Orientada a Objetos -


# ============================================================
# - QUESTÃO 6 - Classe Aluno -
# ============================================================

class Aluno:
    def __init__(self, nome: str, matricula: str) -> None:
        self.nome = nome
        self.matricula = matricula
        self.notas: list[float] = []

    def lancar_nota(self, valor: float) -> None:
        self.notas.append(valor)

    def media(self) -> float:
        if not self.notas:
            return 0.0

        return sum(self.notas) / len(self.notas)

    def aprovado(self) -> bool:
        return self.media() >= 6

    def __str__(self) -> str:
        return (
            f"{self.nome} ({self.matricula}) "
            f"— média {self.media():.1f}"
        )
