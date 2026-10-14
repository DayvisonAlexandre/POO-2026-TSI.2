# ============================================================
# - 01. MIXIN PARA EXPORTAÇÃO CSV -
# ============================================================

class ExportavelCSV:


    def linha_csv(self):
        valores = vars(self).values()
        return ",".join(str(valor) for valor in valores)


# ============================================================
# - 02. SISTEMA BANCÁRIO: CLASSES PRINCIPAIS -
# ============================================================

class Funcionario(ExportavelCSV):
    def __init__(self, nome: str, matricula: str) -> None:
        self._nome = nome
        self._matricula = matricula

    @property
    def nome(self):
        return self._nome

    @property
    def matricula(self):
        return self._matricula


class Autenticavel:
    def __init__(self) -> None:
        self._senha = ""

    def cadastrar_senha(self, senha: str) -> None:
        self._senha = senha

    def autenticar(self, senha: str) -> bool:
        return self._senha == senha


# ============================================================
# - 03. HERANÇA MÚLTIPLA: GERENTE E DIRETOR -
# ============================================================

class Gerente(Funcionario, Autenticavel):
    def __init__(self, nome: str, matricula: str) -> None:
        Funcionario.__init__(self, nome, matricula)
        Autenticavel.__init__(self)


class Diretor(Funcionario, Autenticavel):
    def __init__(self, nome: str, matricula: str) -> None:
        Funcionario.__init__(self, nome, matricula)
        Autenticavel.__init__(self)


# ============================================================
# - 04. CLIENTE: AUTENTICAÇÃO SEM SER FUNCIONÁRIO -
# ============================================================

class Cliente(Autenticavel):
    def __init__(self, nome: str) -> None:
        super().__init__()
        self._nome = nome

    @property
    def nome(self):
        return self._nome


# ============================================================
# - 05. TESTES DE AUTENTICAÇÃO -
# ============================================================

def testar_sistema_bancario():
    print("=" * 55)
    print("1. TESTES DO SISTEMA BANCÁRIO")
    print("=" * 55)

    gerente = Gerente("Ana", "G001")
    gerente.cadastrar_senha("1234")

    cliente = Cliente("Carlos")
    cliente.cadastrar_senha("abcd")

    diretor = Diretor("Mariana", "D001")
    diretor.cadastrar_senha("5678")

    print("Gerente autenticado:",
          gerente.autenticar("1234"))

    print("Gerente com senha incorreta:",
          gerente.autenticar("0000"))

    print("Cliente autenticado:",
          cliente.autenticar("abcd"))

    print("Diretor autenticado:",
          diretor.autenticar("5678"))

    print("Gerente é funcionário:",
          isinstance(gerente, Funcionario))

    print("Cliente é funcionário:",
          isinstance(cliente, Funcionario))


# ============================================================
# - 06. PROBLEMA DO DIAMANTE: A, B, C E D -
# ============================================================

class A:
    def ola(self) -> None:
        print("Olá de A")


class B(A):
    def ola(self) -> None:
        print("Olá de B")


class C(A):
    def ola(self) -> None:
        print("Olá de C")


class D(B, C):
    pass


def testar_diamante():
    print("\n" + "=" * 55)
    print("2. PROBLEMA DO DIAMANTE: D(B, C)")
    print("=" * 55)

    d = D()
    d.ola()

    print("Ordem MRO:")
    print(" -> ".join(classe.__name__ for classe in D.__mro__))


# ============================================================
# - 07. INVERSÃO DA ORDEM DAS CLASSES-BASE -
# ============================================================

class DInvertida(C, B):
    pass


def testar_mro_invertido():
    print("\n" + "=" * 55)
    print("3. DIAMANTE COM ORDEM INVERTIDA: D(C, B)")
    print("=" * 55)

    d = DInvertida()
    d.ola()

    print("Ordem MRO:")
    print(" -> ".join(
        classe.__name__ for classe in DInvertida.__mro__
    ))


# ============================================================
# - 08. TESTE DO MIXIN EXPORTAVELCSV -
# ============================================================

def testar_exportacao_csv():
    print("\n" + "=" * 55)
    print("4. TESTE DO MIXIN EXPORTAVELCSV")
    print("=" * 55)

    funcionario = Funcionario("João", "F001")

    print("Linha CSV:")
    print(funcionario.linha_csv())

    print("Usa o mixin:",
          isinstance(funcionario, ExportavelCSV))


# ============================================================
# - 09. EXECUÇÃO DOS TESTES -
# ============================================================

if __name__ == "__main__":
    testar_sistema_bancario()
    testar_diamante()
    testar_mro_invertido()
    testar_exportacao_csv()
