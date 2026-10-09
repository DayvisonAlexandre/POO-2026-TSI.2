# E18 - Heranca I
# Programacao Orientada a Objetos (POO)


# ==========================================
# - QUESTOES 01 E 02 - ANIMAL, GATO, CACHORRO E PASSARO -
# ==========================================

class Animal:
    def __init__(self, nome: str, peso: float) -> None:
        self._nome = nome
        self._peso = peso
        self._posicao = 0

    def mover_se(self) -> None:
        self._posicao += 1

    def __str__(self) -> str:
        return (
            f"{self._nome}: peso {self._peso}, "
            f"posicao {self._posicao}"
        )


class Gato(Animal):
    def __init__(self, nome: str, peso: float) -> None:
        super().__init__(nome, peso)

    def miar(self) -> None:
        print("Miau...")


class Cachorro(Animal):
    def __init__(
        self, nome: str, peso: float, raca: str
    ) -> None:
        super().__init__(nome, peso)
        self._raca = raca

    def latir(self) -> None:
        print("Au-au...")


class Passaro(Animal):
    def __init__(
        self, nome: str, peso: float, envergadura: float
    ) -> None:
        super().__init__(nome, peso)
        self._envergadura = envergadura

    def __str__(self) -> str:
        descricao = super().__str__()
        return (
            f"{descricao}, "
            f"envergadura {self._envergadura}"
        )



print("=== ANIMAIS ===")

tom = Gato("Tom", 2.0)
rex = Cachorro("Rex", 12.0, "vira-lata")
pingo = Passaro("Pingo", 0.5, 25.0)

tom.miar()
rex.latir()

animais = [tom, rex, pingo]

print("\nAntes de mover:")
for animal in animais:
    print(animal)

for animal in animais:
    animal.mover_se()

print("\nDepois de mover:")
for animal in animais:
    print(animal)


# ==========================================
# - QUESTAO 03 - FUNCIONARIO E GERENTE -
# ==========================================

class Funcionario:
    def __init__(self, nome: str, salario: float) -> None:
        self._nome = nome
        self._salario = salario

    def apresentar(self) -> str:
        return f"Sou {self._nome}, salario R$ {self._salario:.2f}"


class Gerente(Funcionario):
    def __init__(
        self,
        nome: str,
        salario: float,
        equipe: list[str]
    ) -> None:
        super().__init__(nome, salario)
        self._equipe = equipe

    def apresentar(self) -> str:
        descricao = super().apresentar()
        return (
            f"{descricao}, gerente de uma equipe "
            f"com {len(self._equipe)} integrantes"
        )


print("\n=== FUNCIONARIOS ===")

funcionario = Funcionario("Ana", 2500.00)
gerente = Gerente(
    "Carlos",
    5000.00,
    ["Ana", "Bruno", "Mariana"]
)

print(funcionario.apresentar())
print(gerente.apresentar())


# ==========================================
# - QUESTAO 04 - RETANGULO COLORIDO E QUADRADO -
# ==========================================

class Retangulo:
    def __init__(self, largura: float, altura: float) -> None:
        self.largura = largura
        self.altura = altura

    def calcular_area(self) -> float:
        return self.largura * self.altura


class RetanguloColorido(Retangulo):
    def __init__(
        self,
        largura: float,
        altura: float,
        cor: str
    ) -> None:
        super().__init__(largura, altura)
        self.cor = cor


class Quadrado(Retangulo):
    def __init__(self, lado: float) -> None:
        super().__init__(lado, lado)


print("\n=== FIGURAS GEOMETRICAS ===")

retangulo_colorido = RetanguloColorido(
    5.0, 3.0, "azul"
)
quadrado = Quadrado(4.0)

print(
    f"Retangulo colorido: area = "
    f"{retangulo_colorido.calcular_area()}, "
    f"cor = {retangulo_colorido.cor}"
)

print(f"Quadrado: area = {quadrado.calcular_area()}")

# - Justificativa - Questão 04 — RetanguloColorido e Quadrado -

# RetanguloColorido(Retangulo): sim. Um retângulo colorido continua sendo um retângulo. A subclasse acrescenta a cor sem eliminar o comportamento herdado de cálculo da área.
# Quadrado(Retangulo): sim, no modelo apresentado. Um quadrado é um caso particular de retângulo, com largura e altura iguais. O construtor garante essa igualdade ao receber apenas o lado.
# No código apresentado, o método calcular_area() funciona corretamente para as duas subclasses.
