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
