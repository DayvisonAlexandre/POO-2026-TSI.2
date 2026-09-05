class Pessoa:
    def __init__(self, nome, idade=20, cep=None):
        self.nome = nome
        self._idade = idade
        self.__cep = cep

    def dizerNome(self):
        print(f"Meu nome é {self.nome}")

    def atualizarCEP(self, cep):
        if len(cep) != 8:
            print("Quantidade de dígitos inválida!")
        else:
            self.__cep = cep
            print("CEP atualizado com sucesso!")

    def isAdulto(self) -> bool:
        return True if self._idade >= 18 else False


class Cliente:
    def __init__(self, nome, cpf, renda):
        self.nome = nome
        self.cpf = cpf
        self.renda = renda

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser uma string.")

        if nome.strip() == "":
            raise ValueError("O nome não pode ser vazio.")

        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        if not isinstance(cpf, str):
            raise TypeError("O CPF deve ser uma string.")

        if cpf.strip() == "":
            raise ValueError("O CPF não pode ser vazio.")

        self.__cpf = cpf

    @property
    def renda(self):
        return self.__renda

    @renda.setter
    def renda(self, renda):
        if not isinstance(renda, (int, float)):
            raise TypeError("A renda deve ser um número.")

        if renda < 0:
            raise ValueError("A renda não pode ser negativa.")

        self.__renda = float(renda)


class Pessoa:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getCPF(self):
        return self.__cpf

    def setCPF(self, cpf):
        self.__cpf = cpf


# Criando uma pessoa
p1 = Pessoa("Jose", "123.456.789-00")

print(f"Meu nome é {p1.getNome()}")
print(f"Meu CPF é {p1.getCPF()}")

p1.setCPF("111.222.333-44")

print(f"Meu novo CPF é {p1.getCPF()}")


from cliente import Cliente


print("===================================")
print("      TESTE DA CLASSE CLIENTE")
print("===================================")


# ===================================
# TESTE 1 - Cliente válido
# ===================================

print("\n--- Teste 1: Cliente válido ---")

cliente1 = Cliente(
    "João Silva",
    "123.456.789-00",
    3500.00
)

print(f"Nome: {cliente1.nome}")
print(f"CPF: {cliente1.cpf}")
print(f"Renda: R$ {cliente1.renda:.2f}")


# ===================================
# TESTE 2 - Alterando o nome
# ===================================

print("\n--- Teste 2: Alterando o nome ---")

cliente1.nome = "Maria Silva"

print(f"Novo nome: {cliente1.nome}")


# ===================================
# TESTE 3 - Alterando o CPF
# ===================================

print("\n--- Teste 3: Alterando o CPF ---")

cliente1.cpf = "111.222.333-44"

print(f"Novo CPF: {cliente1.cpf}")


# ===================================
# TESTE 4 - Alterando a renda
# ===================================

print("\n--- Teste 4: Alterando a renda ---")

cliente1.renda = 5000

print(f"Nova renda: R$ {cliente1.renda:.2f}")


# ===================================
# TESTE 5 - Nome inválido
# ===================================

print("\n--- Teste 5: Nome inválido ---")

try:
    cliente1.nome = ""
except ValueError as erro:
    print(f"Erro: {erro}")


# ===================================
# TESTE 6 - CPF inválido
# ===================================

print("\n--- Teste 6: CPF inválido ---")

try:
    cliente1.cpf = ""
except ValueError as erro:
    print(f"Erro: {erro}")


# ===================================
# TESTE 7 - Renda negativa
# ===================================

print("\n--- Teste 7: Renda negativa ---")

try:
    cliente1.renda = -1000
except ValueError as erro:
    print(f"Erro: {erro}")


# ===================================
# TESTE 8 - Renda com texto
# ===================================

print("\n--- Teste 8: Renda com texto ---")

try:
    cliente1.renda = "3000"
except TypeError as erro:
    print(f"Erro: {erro}")


# ===================================
# TESTE 9 - Nome com tipo errado
# ===================================

print("\n--- Teste 9: Nome com tipo errado ---")

try:
    cliente1.nome = 123
except TypeError as erro:
    print(f"Erro: {erro}")


print("\n===================================")
print("          TESTES FINALIZADOS")
print("===================================")
