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


# ============================================================
# - QUESTÃO 7 - Criar 3 alunos e imprimir apenas os aprovados -
# ============================================================

aluno1 = Aluno("Ana", "20261234")
aluno1.lancar_nota(7.0)
aluno1.lancar_nota(8.0)

aluno2 = Aluno("Bruno", "20261235")
aluno2.lancar_nota(5.0)
aluno2.lancar_nota(5.5)

aluno3 = Aluno("Carlos", "20261236")
aluno3.lancar_nota(6.0)
aluno3.lancar_nota(7.0)

alunos = [aluno1, aluno2, aluno3]

print("=== QUESTÃO 7 ===")
print("Alunos aprovados:")

for aluno in alunos:
    if aluno.aprovado():
        print(aluno)
