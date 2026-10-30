# - Questão 01 -

from dataclasses import dataclass


@dataclass
class Produto:
    nome: str
    preco: float
    estoque: int = 0


@dataclass
class ItemPedido:
    produto: Produto
    quantidade: int

    @property
    def subtotal(self) -> float:
        return self.produto.preco * self.quantidade


produto = Produto("Teclado", 120.0, 10)

item = ItemPedido(produto, 2)

print(produto)
print(item)
print("Subtotal:", item.subtotal)

# - Questão 02 -

from dataclasses import dataclass


@dataclass(order=True)
class Musica:
    titulo: str
    artista: str
    duracao_seg: int


playlist = [
    Musica("Yellow", "Coldplay", 269),
    Musica("Numb", "Linkin Park", 185),
    Musica("Believer", "Imagine Dragons", 204)
]

playlist_ordenada = sorted(playlist)

for musica in playlist_ordenada:
    print(musica)

# - Questão 03 -

from dataclasses import dataclass


@dataclass(frozen=True)
class Endereco:
    rua: str
    numero: int
    cidade: str
    estado: str


endereco = Endereco(
    "Rua das Flores",
    100,
    "Parnamirim",
    "RN"
)

print(endereco)

endereco.numero = 200

# - Explicação: O parâmetro frozen=True torna os objetos imutáveis, impedindo a alteração de seus atributos depois da criação.
# Por isso, ao tentar modificar o atributo numero, o Python gera uma exceção chamada FrozenInstanceError. -

# - Questão 04 -

from dataclasses import dataclass, field


@dataclass
class Turma:
    nome: str
    alunos: list[str] = field(default_factory=list)


turma1 = Turma("POO")
turma2 = Turma("Web")

turma1.alunos.append("Ana")
turma1.alunos.append("Carlos")

print("Turma 1:", turma1.alunos)
print("Turma 2:", turma2.alunos)

# - Explicação: O default_factory=list, cria uma lista nova para cada objeto da classe.
# Assim, os alunos adicionados à primeira turma, não aparecem na segunda turma, evitando o compartilhamento indevido de listas entre objetos. -

# - Questão 05 -

# - Explicação: Não, pois uma classe ContaBancaria, possui regras de negócio e precisa proteger seu estado interno, como o saldo.
# Uma classe convencional permite implementar validações, encapsulamento e métodos específicos para depósitos e saques.
# Por isso, é mais adequado utilizar uma classe convencional do que uma dataclass. -
