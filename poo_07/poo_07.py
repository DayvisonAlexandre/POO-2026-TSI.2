# ============================================================
# - exercicío 01 - classe carro -
# ============================================================

class Carro:
    # Construtor da classe
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0
        self.ligado = False

    # Método para ligar o carro
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"O carro {self.marca} {self.modelo} foi ligado.")
        else:
            print(f"O carro {self.marca} {self.modelo} já está ligado.")

    # Método para desligar o carro
    def desligar(self):
        if self.velocidade == 0:
            if self.ligado:
                self.ligado = False
                print(f"O carro {self.marca} {self.modelo} foi desligado.")
            else:
                print(f"O carro {self.marca} {self.modelo} já está desligado.")
        else:
            print("Não é possível desligar o carro enquanto ele estiver em movimento.")

    # Método para acelerar
    def acelerar(self, valor):
        if self.ligado:
            if valor > 0:
                self.velocidade += valor
                print(
                    f"O carro acelerou {valor} km/h. "
                    f"Velocidade atual: {self.velocidade} km/h."
                )
            else:
                print("O valor da aceleração deve ser maior que zero.")
        else:
            print("Não é possível acelerar. O carro está desligado.")

    # Método para frear
    def frear(self, valor):
        if valor > 0:
            self.velocidade -= valor

            # Impede que a velocidade fique negativa
            if self.velocidade < 0:
                self.velocidade = 0

            print(
                f"O carro freou {valor} km/h. "
                f"Velocidade atual: {self.velocidade} km/h."
            )
        else:
            print("O valor da frenagem deve ser maior que zero.")

    # Método para mostrar as informações do carro
    def mostrar_informacoes(self):
        print("\n--- INFORMAÇÕES DO CARRO ---")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.cor}")
        print(f"Velocidade: {self.velocidade} km/h")

        if self.ligado:
            print("Estado: Ligado")
        else:
            print("Estado: Desligado")

# ============================================================
# - programa principal - testando a classe carro -
# ============================================================

print("=" * 50)
print("TESTE DA CLASSE CARRO")
print("=" * 50)

# Criando um objeto da classe Carro
carro1 = Carro(
    marca="Toyota",
    modelo="Corolla",
    ano=2024,
    cor="Prata"
)

# Mostrando as informações iniciais
carro1.mostrar_informacoes()

# Testando as ações do carro
print("\n--- AÇÕES DO CARRO ---")

carro1.ligar()
carro1.acelerar(30)
carro1.acelerar(20)
carro1.frear(15)

# Mostrando novamente as informações
carro1.mostrar_informacoes()

# Freando completamente
carro1.frear(35)

# Desligando o carro
carro1.desligar()

# Mostrando o estado final
carro1.mostrar_informacoes()

# ============================================================
# - exercicío 02 - classe cachorro -
# ============================================================

class Cachorro:
    # Construtor da classe
    def __init__(self, nome, raca, idade, cor):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.cor = cor
        self.energia = 100

    # Método para o cachorro latir
    def latir(self):
        print(f"{self.nome} está latindo: Au au!")

    # Método para o cachorro comer
    def comer(self):
        if self.energia < 100:
            self.energia += 20

            # Impede que a energia ultrapasse 100
            if self.energia > 100:
                self.energia = 100

            print(
                f"{self.nome} comeu e recuperou energia. "
                f"Energia atual: {self.energia}%."
            )
        else:
            print(f"{self.nome} já está com a energia completa.")

    # Método para o cachorro brincar
    def brincar(self):
        if self.energia >= 20:
            self.energia -= 20
            print(
                f"{self.nome} está brincando. "
                f"Energia atual: {self.energia}%."
            )
        else:
            print(
                f"{self.nome} está cansado e não tem energia suficiente "
                "para brincar."
            )

    # Método para o cachorro dormir
    def dormir(self):
        self.energia = 100
        print(
            f"{self.nome} dormiu e recuperou toda a energia. "
            f"Energia atual: {self.energia}%."
        )

    # Método para mostrar as informações do cachorro
    def mostrar_informacoes(self):
        print("\n--- INFORMAÇÕES DO CACHORRO ---")
        print(f"Nome: {self.nome}")
        print(f"Raça: {self.raca}")
        print(f"Idade: {self.idade} anos")
        print(f"Cor: {self.cor}")
        print(f"Energia: {self.energia}%")

# ============================================================
# - programa principal - testando a classe cachorro -
# ============================================================

print("\n" + "=" * 50)
print("TESTE DA CLASSE CACHORRO")
print("=" * 50)

# Criando um objeto da classe Cachorro
cachorro1 = Cachorro(
    nome="Rex",
    raca="Pastor Alemão",
    idade=3,
    cor="Marrom"
)

# Mostrando as informações iniciais
cachorro1.mostrar_informacoes()

# Testando as ações do cachorro
print("\n--- AÇÕES DO CACHORRO ---")

cachorro1.latir()
cachorro1.brincar()
cachorro1.brincar()
cachorro1.comer()
cachorro1.dormir()

# Mostrando o estado final
cachorro1.mostrar_informacoes()
