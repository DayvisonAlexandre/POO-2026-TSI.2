# ============================================================
# Exercício 01
# __str__ e __repr__ na classe Tarefa
# ============================================================

class Tarefa:
    def __init__(self, descricao, concluida=False):
        self.descricao = descricao
        self.concluida = concluida

    def __str__(self):
        """
        Retorna uma representação amigável da tarefa,
        usada principalmente por print().
        """
        status = "Concluída" if self.concluida else "Pendente"
        return f"Tarefa: {self.descricao} | Status: {status}"

    def __repr__(self):
        """
        Retorna uma representação mais técnica da tarefa,
        útil para depuração e para representar o objeto.
        """
        return (
            f"Tarefa(descricao={self.descricao!r}, "
            f"concluida={self.concluida!r})"
        )


# ============================================================
# Exercício 02
# __eq__ na classe ContaBancaria
# ============================================================

class ContaBancaria:
    def __init__(self, numero, titular, saldo=0.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def __eq__(self, outra):
        """
        Duas contas são consideradas iguais quando
        possuem o mesmo número de conta.
        """
        if not isinstance(outra, ContaBancaria):
            return NotImplemented

        return self.numero == outra.numero

    def __str__(self):
        return (
            f"Conta {self.numero} | "
            f"Titular: {self.titular} | "
            f"Saldo: R$ {self.saldo:.2f}"
        )


# ============================================================
# Exercício 03
# __lt__ na classe Pessoa
# Ordenação pela idade
# ============================================================

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __lt__(self, outra):
        """
        Define que uma pessoa é "menor" que outra
        quando possui idade menor.
        """
        if not isinstance(outra, Pessoa):
            return NotImplemented

        return self.idade < outra.idade

    def __str__(self):
        return f"{self.nome} - {self.idade} anos"

    def __repr__(self):
        return f"Pessoa(nome={self.nome!r}, idade={self.idade!r})"


# ============================================================
# Programa Principal
# ============================================================

print("=" * 60)
print("PRÁTICA - EXERCÍCIOS EM SALA")
print("=" * 60)


# ============================================================
# Exercício 01
# ============================================================

print("\n" + "=" * 60)
print("EXERCÍCIO 1 - __str__ E __repr__")
print("=" * 60)

tarefa1 = Tarefa("Estudar Python", False)
tarefa2 = Tarefa("Fazer o trabalho", True)

print("\nUsando print() diretamente:")
print(tarefa1)
print(tarefa2)

print("\nUsando __repr__:")
print(repr(tarefa1))
print(repr(tarefa2))

lista_tarefas = [tarefa1, tarefa2]

print("\nLista de tarefas:")
print(lista_tarefas)


# ============================================================
# Exercício 02
# ============================================================

print("\n" + "=" * 60)
print("EXERCÍCIO 2 - __eq__ EM CONTABANCARIA")
print("=" * 60)

conta1 = ContaBancaria(
    numero="001",
    titular="João",
    saldo=1500.00
)

conta2 = ContaBancaria(
    numero="002",
    titular="Maria",
    saldo=1500.00
)

conta3 = ContaBancaria(
    numero="001",
    titular="Outra Pessoa",
    saldo=500.00
)

print("\nContas cadastradas:")
print(conta1)
print(conta2)
print(conta3)

print("\nComparações:")

print(
    f"conta1 == conta2: {conta1 == conta2}"
)

print(
    f"conta1 == conta3: {conta1 == conta3}"
)

print(
    f"conta2 == conta3: {conta2 == conta3}"
)

print("\nObservação:")
print(
    "conta1 e conta3 possuem saldos e titulares diferentes, "
    "mas possuem o mesmo número."
)
print(
    "Por isso, são consideradas contas iguais."
)


# ============================================================
# Exercício 03
# ============================================================

print("\n" + "=" * 60)
print("EXERCÍCIO 3 - __lt__ E ORDENAÇÃO POR IDADE")
print("=" * 60)

pessoas = [
    Pessoa("Carlos", 25),
    Pessoa("Ana", 18),
    Pessoa("Marcos", 40),
    Pessoa("Julia", 22),
    Pessoa("Pedro", 30)
]

print("\nLista original:")

for pessoa in pessoas:
    print(pessoa)

pessoas_ordenadas = sorted(pessoas)

print("\nLista ordenada pela idade:")

for pessoa in pessoas_ordenadas:
    print(pessoa)


# ============================================================
# Testes Extras dos Operadores
# ============================================================

print("\n" + "=" * 60)
print("TESTES DOS OPERADORES")
print("=" * 60)

print("\nTeste do __str__:")
print(tarefa1)

print("\nTeste do __repr__:")
print(repr(tarefa1))

print("\nTeste do __eq__:")
print(f"Conta 1 == Conta 3? {conta1 == conta3}")

print("\nTeste do __lt__:")
pessoa_a = Pessoa("Lucas", 20)
pessoa_b = Pessoa("Gabriel", 25)

print(f"{pessoa_a} < {pessoa_b}? {pessoa_a < pessoa_b}")

print("\nOrdenação com sorted():")
print(sorted(pessoas))

# ============================================================
# Discussão
# ============================================================

print("\n" + "=" * 60)
print("DISCUSSÃO")
print("=" * 60)

print("""
Por que comparar contas pelo número e não pelo saldo?

O número da conta é o identificador da conta bancária.
Ele serve para identificar uma conta específica dentro do
sistema.

O saldo, por outro lado, é apenas uma característica da
conta e pode mudar várias vezes durante sua utilização.

Por exemplo, duas contas podem ter o mesmo saldo de
R$ 1.500,00 e ainda assim serem contas diferentes.

Da mesma forma, duas referências podem representar a mesma
conta mesmo que o saldo tenha mudado.

Por isso, o método __eq__ foi implementado comparando o
atributo numero e não o atributo saldo.

Isso mostra que a igualdade de objetos pode ser definida
de acordo com uma identidade lógica do domínio.

No caso da ContaBancaria, o número funciona como essa
identidade lógica.

Assim:

    conta1 == conta3

retorna True quando os números são iguais, mesmo que
titulares e saldos sejam diferentes.
""")


print("=" * 60)
print("FIM DO PROGRAMA")
print("=" * 60)
