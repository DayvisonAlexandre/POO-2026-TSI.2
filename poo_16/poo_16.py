# Resolução — Associação e Agregação

## 1. Classe Motorista e classe Veiculo — Associação

class Veiculo:
    def __init__(self, modelo: str) -> None:
        self._modelo = modelo

    def __str__(self) -> str:
        return self._modelo


class Motorista:
    def __init__(self, nome: str) -> None:
        self._nome = nome

    def dirigir(self, veiculo: Veiculo) -> None:
        print(f"{self._nome} dirige o veículo {veiculo}")


# Teste
motorista = Motorista("João")
carro = Veiculo("Toyota Corolla")

motorista.dirigir(carro)

# 2. Playlist e Musica — Agregação

class Musica:
    def __init__(self, titulo: str, artista: str, duracao: int) -> None:
        self._titulo = titulo
        self._artista = artista
        self._duracao = duracao

    def __str__(self) -> str:
        minutos = self._duracao // 60
        segundos = self._duracao % 60
        return f"{self._titulo} - {self._artista} ({minutos}:{segundos:02d})"

    def get_duracao(self) -> int:
        return self._duracao


class Playlist:
    def __init__(self, nome: str) -> None:
        self._nome = nome
        self._musicas: list[Musica] = []

    def adicionar(self, musica: Musica) -> None:
        self._musicas.append(musica)

    def remover(self, musica: Musica) -> None:
        if musica in self._musicas:
            self._musicas.remove(musica)

    def duracao_total(self) -> int:
        return sum(musica.get_duracao() for musica in self._musicas)

    def listar(self) -> None:
        print(f"Playlist: {self._nome}")

        for musica in self._musicas:
            print(musica)


# Teste
musica1 = Musica("Musica 1", "Artista 1", 180)
musica2 = Musica("Musica 2", "Artista 2", 240)
musica3 = Musica("Musica 3", "Artista 3", 200)

playlist = Playlist("Minha Playlist")

playlist.adicionar(musica1)
playlist.adicionar(musica2)
playlist.adicionar(musica3)

playlist.listar()

print(f"Duração total: {playlist.duracao_total()} segundos")

playlist.remover(musica2)

print("\nDepois de remover uma música:")
playlist.listar()
print(f"Duração total: {playlist.duracao_total()} segundos")

# 3. Playlist e CaixaDeSom — Associação

class CaixaDeSom:
    def __init__(self, modelo: str) -> None:
        self._modelo = modelo

    def tocar(self, musica: Musica) -> None:
        print(f"Caixa de som {self._modelo} tocando: {musica}")


class Playlist:
    def __init__(self, nome: str) -> None:
        self._nome = nome
        self._musicas: list[Musica] = []

    def adicionar(self, musica: Musica) -> None:
        self._musicas.append(musica)

    def tocar(self, caixa_de_som: CaixaDeSom) -> None:
        for musica in self._musicas:
            caixa_de_som.tocar(musica)


# Exemplo:


musica1 = Musica("Musica 1", "Artista 1", 180)
musica2 = Musica("Musica 2", "Artista 2", 240)

playlist = Playlist("Minha Playlist")

playlist.adicionar(musica1)
playlist.adicionar(musica2)

caixa = CaixaDeSom("JBL")

playlist.tocar(caixa)

# 4. UML dos dois cenários

## 4.1 Motorista e Veiculo

# Como é associação, utiliza-se uma linha/seta contínua:


#┌──────────────┐              ┌──────────────┐
#│  Motorista   │─────────────>│   Veiculo    │
#├──────────────┤              ├──────────────┤
#│ - nome       │              │ - modelo     │
#├──────────────┤              ├──────────────┤
#│ + dirigir()  │              │              │
#└──────────────┘              └──────────────┘


# A direção da relação indica:

# Motorista usa Veiculo.


## 4.2 Playlist e Musica

# Como é agregação, utiliza-se o losango aberto (◇) no lado do todo:


#┌─────────────────┐        ◇──────────────┐
#│    Playlist     │                       │
#├─────────────────┤                       │
#│ - nome          │                       │
#│ - musicas       │                       │
#├─────────────────┤                       │
#│ + adicionar()   │                       │
#│ + remover()     │                       │
#│ + duracao_total()│                      │
#└─────────────────┘                       │
#                                          │
#                                  ┌───────▼────────┐
#                                  │     Musica     │
#                                  ├────────────────┤
#                                  │ - titulo       │
#                                  │ - artista      │
#                                  │ - duracao      │
#                                  └────────────────┘


# Ou, de maneira simplificada:


# Playlist ◇──────── Musica


# O losango aberto fica do lado da `Playlist`, porque ela é o todo, enquanto `Musica` representa a parte.



# 5. Relação entre Playlist e CaixaDeSom

#A UML fica:


#┌─────────────────┐              ┌─────────────────┐
#│    Playlist     │─────────────>│   CaixaDeSom   │
#├─────────────────┤              ├─────────────────┤
#│ - nome          │              │ - modelo        │
#│ - musicas       │              ├─────────────────┤
#├─────────────────┤              │ + tocar()       │
#│ + tocar()       │              └─────────────────┘
#└─────────────────┘


# É uma associação, e não agregação.

# Motivo:


# playlist.tocar(caixa)


# A caixa é passada para o método e utilizada durante a operação. A playlist não precisa manter uma referência permanente para ela.



# 6. Biblioteca e Livro

# Considerando os critérios apresentados, a relação entre `Biblioteca` e `Livro` deve ser analisada, pois
# Se a `Biblioteca` mantém os livros em um atributo/coleção, então temos agregação.

# Exemplo:


# class Livro:
#    def __init__(self, titulo: str) -> None:
#        self._titulo = titulo
#
#    def __str__(self) -> str:
#        return self._titulo


# class Biblioteca:
#    def __init__(self) -> None:
#        self._livros: list[Livro] = []
#
#    def adicionar(self, livro: Livro) -> None:
#        self._livros.append(livro)0
#
#    def remover(self, livro: Livro) -> None:
#        if livro in self._livros:
#            self._livros.remove(livro)
#
#    def listar(self) -> None:
#        for livro in self._livros:
#            print(livro)


#Uso:


# livro1 = Livro("Livro A")
# livro2 = Livro("Livro B")

# biblioteca = Biblioteca()

# biblioteca.adicionar(livro1)
# biblioteca.adicionar(livro2)

# biblioteca.listar()


# Nesse modelo:

# Biblioteca ◇──────── Livro

# Relação: Agregação.

# Isso acontece porque os livros existem independentemente da biblioteca. Eles são criados fora:


# livro1 = Livro("Livro A")


# e depois são adicionados à biblioteca:


# biblioteca.adicionar(livro1)
