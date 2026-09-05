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
