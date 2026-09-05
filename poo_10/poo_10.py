from abc import ABC, abstractmethod


# ============================================================
# CLASSE PESSOA
# ============================================================

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def apresentar_informacoes(self):
        print(f"Pessoa: {self.nome}")


# ============================================================
# CLASSE LÂMPADA
# ============================================================

class Lampada:
    def __init__(self, identificacao):
        self.identificacao = identificacao
        self.acessa = False

    def acender(self):
        if self.acessa:
            print(f"Lâmpada {self.identificacao} já está acesa.")
        else:
            self.acessa = True
            print(f"Lâmpada {self.identificacao} foi acesa.")

    def apagar(self):
        if not self.acessa:
            print(f"Lâmpada {self.identificacao} já está apagada.")
        else:
            self.acessa = False
            print(f"Lâmpada {self.identificacao} foi apagada.")

    def apresentar_informacoes(self):
        estado = "acesa" if self.acessa else "apagada"
        print(f"Lâmpada {self.identificacao}: {estado}.")


# ============================================================
# CLASSE AR-CONDICIONADO
# ============================================================

class ArCondicionado:
    def __init__(self):
        self.ligado = False

    def ligar(self):
        if self.ligado:
            print("Ar-condicionado já está ligado.")
        else:
            self.ligado = True
            print("Ar-condicionado foi ligado.")

    def desligar(self):
        if not self.ligado:
            print("Ar-condicionado já está desligado.")
        else:
            self.ligado = False
            print("Ar-condicionado foi desligado.")

    def apresentar_informacoes(self):
        estado = "ligado" if self.ligado else "desligado"
        print(f"Ar-condicionado: {estado}.")


# ============================================================
# CLASSE INTERRUPTOR
# ============================================================

class Interruptor:
    def __init__(self, identificacao, componente):
        self.identificacao = identificacao
        self.componente = componente

    def acionar(self):
        # Interruptor de lâmpada
        if isinstance(self.componente, Lampada):
            if self.componente.acessa:
                self.componente.apagar()
            else:
                self.componente.acender()

        # Interruptor de ar-condicionado
        elif isinstance(self.componente, ArCondicionado):
            if self.componente.ligado:
                self.componente.desligar()
            else:
                self.componente.ligar()

    def apresentar_informacoes(self):
        tipo = type(self.componente).__name__
        print(
            f"Interruptor {self.identificacao}: "
            f"controla {tipo}."
        )


# ============================================================
# CLASSE ABSTRATA FECHADURA
# ============================================================

class Fechadura(ABC):
    def __init__(self, chave):
        self.chave = chave

    @abstractmethod
    def abrir(self, chave=None, senha=None):
        pass

    @abstractmethod
    def apresentar_informacoes(self):
        pass


# ============================================================
# FECHADURA SIMPLES
# ============================================================

class FechaduraSimples(Fechadura):

    def abrir(self, chave=None, senha=None):
        if chave == self.chave:
            return True
        return False

    def apresentar_informacoes(self):
        print("Fechadura simples: abertura somente com chave.")


# ============================================================
# FECHADURA INTELIGENTE
# ============================================================

class FechaduraInteligente(Fechadura):
    def __init__(self, chave, senha):
        super().__init__(chave)
        self.senha = senha

    def abrir(self, chave=None, senha=None):
        if chave == self.chave:
            return True

        if senha == self.senha:
            return True

        return False

    def apresentar_informacoes(self):
        print(
            "Fechadura inteligente: abertura com chave ou senha."
        )


# ============================================================
# CLASSE PORTA
# ============================================================

class Porta:
    def __init__(self, identificacao, comodo, fechadura):
        self.identificacao = identificacao
        self.comodo = comodo
        self.fechadura = fechadura
        self.aberta = False

    def abrir(self, pessoa, chave=None, senha=None):
        if self.aberta:
            print(
                f"{pessoa.nome}: A porta {self.identificacao} "
                f"já está aberta."
            )
            return

        if self.fechadura.abrir(chave, senha):
            self.aberta = True
            print(
                f"{pessoa.nome}: A porta {self.identificacao} "
                f"foi aberta. Ela pertence ao cômodo "
                f"'{self.comodo.nome}'."
            )
        else:
            print(
                f"{pessoa.nome}: Não foi possível abrir a porta "
                f"{self.identificacao}. Chave ou senha incorreta."
            )

    def fechar(self, pessoa):
        if not self.aberta:
            print(
                f"{pessoa.nome}: A porta {self.identificacao} "
                f"já está fechada."
            )
        else:
            self.aberta = False
            print(
                f"{pessoa.nome}: A porta {self.identificacao} "
                f"foi fechada."
            )

    def apresentar_informacoes(self):
        estado = "aberta" if self.aberta else "fechada"

        print(
            f"Porta {self.identificacao}: "
            f"pertence ao cômodo '{self.comodo.nome}', "
            f"está {estado}."
        )

        self.fechadura.apresentar_informacoes()


# ============================================================
# CLASSE CÔMODO
# ============================================================

class Comodo:
    def __init__(self, nome, cor, possui_ar_condicionado=False):
        self.nome = nome
        self.cor = cor
        self.lampadas = []
        self.interruptores = []
        self.portas = []

        if possui_ar_condicionado:
            self.ar_condicionado = ArCondicionado()
        else:
            self.ar_condicionado = None

    def adicionar_lampada(self, lampada):
        self.lampadas.append(lampada)

    def adicionar_interruptor(self, interruptor):
        self.interruptores.append(interruptor)

    def adicionar_porta(self, porta):
        self.portas.append(porta)

    def apresentar_informacoes(self):
        print("\n" + "=" * 60)
        print(f"CÔMODO: {self.nome}")
        print(f"Cor: {self.cor}")

        print(f"Lâmpadas: {len(self.lampadas)}")
        for lampada in self.lampadas:
            lampada.apresentar_informacoes()

        print(f"Interruptores: {len(self.interruptores)}")
        for interruptor in self.interruptores:
            interruptor.apresentar_informacoes()

        print(f"Portas: {len(self.portas)}")
        for porta in self.portas:
            porta.apresentar_informacoes()

        if self.ar_condicionado is not None:
            self.ar_condicionado.apresentar_informacoes()
        else:
            print("Ar-condicionado: não possui.")

        print("=" * 60)


# ============================================================
# CLASSE CASA
# ============================================================

class Casa:
    LIMITE_COMODOS = 10

    def __init__(self, endereco):
        self.endereco = endereco
        self.comodos = []
        self.pessoas = []

    def adicionar_comodo(self, comodo):
        if len(self.comodos) >= self.LIMITE_COMODOS:
            print(
                "Não é possível adicionar mais cômodos. "
                "O limite máximo é 10."
            )
            return False

        # Cada cômodo deve possuir pelo menos uma porta.
        if len(comodo.portas) < 1:
            print(
                f"O cômodo '{comodo.nome}' precisa possuir "
                "pelo menos uma porta."
            )
            return False

        self.comodos.append(comodo)

        print(
            f"Cômodo '{comodo.nome}' adicionado à casa."
        )

        return True

    def adicionar_pessoa(self, pessoa):
        self.pessoas.append(pessoa)
        print(
            f"Pessoa '{pessoa.nome}' entrou na casa."
        )

    def buscar_comodo(self, nome):
        for comodo in self.comodos:
            if comodo.nome.lower() == nome.lower():
                return comodo

        return None

    def apresentar_informacoes(self):
        print("\n")
        print("#" * 60)
        print("INFORMAÇÕES DA CASA")
        print("#" * 60)
        print(f"Endereço: {self.endereco}")
        print(f"Quantidade de cômodos: {len(self.comodos)}")
        print(f"Quantidade de pessoas: {len(self.pessoas)}")

        print("\nCÔMODOS:")
        for comodo in self.comodos:
            comodo.apresentar_informacoes()

        print("\nPESSOAS:")
        for pessoa in self.pessoas:
            pessoa.apresentar_informacoes()

        print("#" * 60)


# ============================================================
# FUNÇÕES AUXILIARES PARA CRIAÇÃO
# ============================================================

def ler_inteiro(mensagem, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensagem))

            if minimo is not None and valor < minimo:
                print(f"Digite um valor maior ou igual a {minimo}.")
                continue

            if maximo is not None and valor > maximo:
                print(f"Digite um valor menor ou igual a {maximo}.")
                continue

            return valor

        except ValueError:
            print("Digite um número inteiro válido.")


def ler_sim_nao(mensagem):
    while True:
        resposta = input(mensagem).strip().lower()

        if resposta in ("s", "sim"):
            return True

        if resposta in ("n", "nao", "não"):
            return False

        print("Digite S para sim ou N para não.")


# ============================================================
# CRIAÇÃO DA CASA PELO USUÁRIO
# ============================================================

def criar_casa_pelo_usuario():
    print("\n" + "=" * 60)
    print("CONFIGURAÇÃO DA CASA")
    print("=" * 60)

    endereco = input("Digite o endereço da casa: ")

    casa = Casa(endereco)

    quantidade = ler_inteiro(
        "Quantidade de cômodos (1 a 10): ",
        1,
        10
    )

    for numero_comodo in range(1, quantidade + 1):

        print("\n" + "-" * 60)
        print(f"CADASTRO DO CÔMODO {numero_comodo}")
        print("-" * 60)

        nome = input("Nome do cômodo: ")
        cor = input("Cor do cômodo: ")

        possui_ar = ler_sim_nao(
            "Possui ar-condicionado? (S/N): "
        )

        comodo = Comodo(
            nome,
            cor,
            possui_ar
        )

        # Pelo menos uma lâmpada para existir um interruptor
        # de iluminação no cômodo.
        quantidade_lampadas = ler_inteiro(
            "Quantidade de lâmpadas (mínimo 1): ",
            1
        )

        for numero_lampada in range(1, quantidade_lampadas + 1):
            lampada = Lampada(
                f"{nome}-L{numero_lampada}"
            )

            comodo.adicionar_lampada(lampada)

            interruptor = Interruptor(
                f"{nome}-I{numero_lampada}",
                lampada
            )

            comodo.adicionar_interruptor(interruptor)

        # Interruptor do ar-condicionado
        if possui_ar:
            interruptor_ar = Interruptor(
                f"{nome}-I-AR",
                comodo.ar_condicionado
            )

            comodo.adicionar_interruptor(interruptor_ar)

        # Pelo menos uma porta
        quantidade_portas = ler_inteiro(
            "Quantidade de portas (mínimo 1): ",
            1
        )

        for numero_porta in range(1, quantidade_portas + 1):

            print(
                f"\nConfiguração da porta {numero_porta}"
            )

            identificacao = (
                f"{nome}-P{numero_porta}"
            )

            print("Tipos de fechadura:")
            print("1 - Fechadura simples")
            print("2 - Fechadura inteligente")

            tipo_fechadura = ler_inteiro(
                "Escolha o tipo: ",
                1,
                2
            )

            chave = input(
                "Digite a chave correta da fechadura: "
            )

            if tipo_fechadura == 1:
                fechadura = FechaduraSimples(chave)

            else:
                senha = input(
                    "Digite a senha da fechadura inteligente: "
                )

                fechadura = FechaduraInteligente(
                    chave,
                    senha
                )

            porta = Porta(
                identificacao,
                comodo,
                fechadura
            )

            comodo.adicionar_porta(porta)

        casa.adicionar_comodo(comodo)

    return casa


# ============================================================
# CENÁRIO DE TESTES
# ============================================================

def executar_cenario_de_testes(casa):
    print("\n\n")
    print("#" * 70)
    print("INÍCIO DO CENÁRIO DE TESTES")
    print("#" * 70)

    # --------------------------------------------------------
    # TESTE 1 - Criar pessoa
    # --------------------------------------------------------

    print("\n[TESTE 1] Criação e entrada de pessoa")

    pessoa = Pessoa("João")

    casa.adicionar_pessoa(pessoa)

    print("Resultado:")
    pessoa.apresentar_informacoes()

    # --------------------------------------------------------
    # TESTE 2 - Informações da casa
    # --------------------------------------------------------

    print("\n[TESTE 2] Apresentação das informações da casa")

    casa.apresentar_informacoes()

    # --------------------------------------------------------
    # TESTE 3 - Acender e apagar lâmpadas
    # --------------------------------------------------------

    print("\n[TESTE 3] Acionamento dos interruptores das lâmpadas")

    for comodo in casa.comodos:

        print(
            f"\nTestando lâmpadas do cômodo "
            f"'{comodo.nome}':"
        )

        for interruptor in comodo.interruptores:

            if isinstance(
                interruptor.componente,
                Lampada
            ):
                print(
                    f"\nAcionando {interruptor.identificacao}..."
                )

                interruptor.acionar()

                print(
                    f"Acionando novamente "
                    f"{interruptor.identificacao}..."
                )

                interruptor.acionar()

    # --------------------------------------------------------
    # TESTE 4 - Ar-condicionado
    # --------------------------------------------------------

    print(
        "\n[TESTE 4] Teste dos ar-condicionados"
    )

    for comodo in casa.comodos:

        if comodo.ar_condicionado is not None:

            print(
                f"\nTestando ar-condicionado "
                f"do cômodo '{comodo.nome}':"
            )

            for interruptor in comodo.interruptores:

                if isinstance(
                    interruptor.componente,
                    ArCondicionado
                ):
                    interruptor.acionar()
                    interruptor.acionar()

    # --------------------------------------------------------
    # TESTE 5 - Portas e fechaduras
    # --------------------------------------------------------

    print("\n[TESTE 5] Teste das portas")

    for comodo in casa.comodos:

        print(
            f"\nTestando portas do cômodo "
            f"'{comodo.nome}':"
        )

        for porta in comodo.portas:

            print(
                f"\nPorta: {porta.identificacao}"
            )

            # Primeiro teste com informação da porta
            porta.apresentar_informacoes()

            # Teste com chave errada
            print("\nTentativa com chave incorreta:")

            porta.abrir(
                pessoa,
                chave="CHAVE_INCORRETA"
            )

            # Teste com chave correta
            print("\nTentativa com chave correta:")

            porta.abrir(
                pessoa,
                chave=porta.fechadura.chave
            )

            # Fecha a porta
            porta.fechar(pessoa)

            # Se for inteligente, testa senha
            if isinstance(
                porta.fechadura,
                FechaduraInteligente
            ):
                print(
                    "\nTentativa com senha correta:"
                )

                porta.abrir(
                    pessoa,
                    senha=porta.fechadura.senha
                )

                porta.fechar(pessoa)

    # --------------------------------------------------------
    # TESTE 6 - Verificação do limite de cômodos
    # --------------------------------------------------------

    print(
        "\n[TESTE 6] Verificação do limite máximo de 10 cômodos"
    )

    print(
        f"A casa possui atualmente "
        f"{len(casa.comodos)} cômodo(s)."
    )

    if len(casa.comodos) <= Casa.LIMITE_COMODOS:
        print(
            "OK: A quantidade de cômodos está dentro "
            "do limite permitido de 10."
        )
    else:
        print(
            "ERRO: A casa ultrapassou o limite de 10 cômodos."
        )

    # --------------------------------------------------------
    # TESTE 7 - Método de informações de todos os objetos
    # --------------------------------------------------------

    print(
        "\n[TESTE 7] Apresentação das informações dos objetos"
    )

    for comodo in casa.comodos:

        print(
            f"\n--- Informações do cômodo "
            f"'{comodo.nome}' ---"
        )

        comodo.apresentar_informacoes()

    print("\n")
    print("#" * 70)
    print("FIM DO CENÁRIO DE TESTES")
    print("#" * 70)


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():

    print("=" * 70)
    print("SIMULAÇÃO DE UM AMBIENTE DE UMA CASA")
    print("=" * 70)

    casa = criar_casa_pelo_usuario()

    executar_cenario_de_testes(casa)


if __name__ == "__main__":
    main()
