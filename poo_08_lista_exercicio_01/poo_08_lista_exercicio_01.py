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


# ============================================================
# - QUESTÃO 8 - Classe Retangulo -
# ============================================================

class Retangulo:
    def __init__(self, base: float, altura: float) -> None:
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return self.base * self.altura

    def perimetro(self) -> float:
        return 2 * (self.base + self.altura)

    def __eq__(self, outro: object) -> bool:
        if not isinstance(outro, Retangulo):
            return NotImplemented

        return (
            self.base == outro.base
            and self.altura == outro.altura
        )


print("\n=== QUESTÃO 8 ===")

retangulo1 = Retangulo(5.0, 3.0)
retangulo2 = Retangulo(5.0, 3.0)
retangulo3 = Retangulo(4.0, 3.0)

print(f"Área do retângulo 1: {retangulo1.area():.2f}")
print(f"Perímetro do retângulo 1: {retangulo1.perimetro():.2f}")
print(f"Retângulo 1 == Retângulo 2? {retangulo1 == retangulo2}")
print(f"Retângulo 1 == Retângulo 3? {retangulo1 == retangulo3}")
