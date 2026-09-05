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
