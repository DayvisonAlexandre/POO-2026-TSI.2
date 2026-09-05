# ============================================================
# CLASSE PRODUTO
# ============================================================

class Produto:
    # (1) Contador de classe
    total_cadastrados = 0

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

        # Incrementa o total sempre que um produto é criado
        Produto.total_cadastrados += 1

    # (2) Cria um Produto a partir de uma string CSV
    @classmethod
    def de_csv(cls, dados):
        nome, preco, quantidade = dados.split(";")

        produto = cls(
            nome,
            float(preco),
            int(quantidade)
        )

        print(f"\nProduto criado pelo CSV:")
        print(produto)

        return produto

    # (3) Valida se o preço é maior que zero
    @staticmethod
    def validar_preco(valor):
        resultado = valor > 0

        print(f"Validando preço R$ {valor:.2f}: {resultado}")

        return resultado

    def __str__(self):
        return (
            f"Produto: {self.nome} | "
            f"Preço: R$ {self.preco:.2f} | "
            f"Quantidade: {self.quantidade}"
        )


# ============================================================
# CLASSE TEMPERATURA
# ============================================================

class Temperatura:

    def __init__(self, celsius):
        # A temperatura é sempre armazenada em Celsius
        self.celsius = celsius

    @classmethod
    def de_celsius(cls, valor):
        temperatura = cls(valor)

        print(
            f"\nTemperatura criada a partir de Celsius: "
            f"{valor:.2f} °C"
        )

        return temperatura

    @classmethod
    def de_fahrenheit(cls, valor):
        # Conversão de Fahrenheit para Celsius
        celsius = (valor - 32) * 5 / 9

        temperatura = cls(celsius)

        print(
            f"\nTemperatura criada a partir de Fahrenheit: "
            f"{valor:.2f} °F = {celsius:.2f} °C"
        )

        return temperatura

    def __str__(self):
        return f"{self.celsius:.2f} °C"
