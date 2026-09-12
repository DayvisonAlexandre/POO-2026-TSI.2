# ============================================================
# Exercício 01
# __str__ e __repr__ na classe Tarefa
# ============================================================

class Tarefa:
    def __init__(self, descricao, concluida=False):
        self.descricao = descricao
        self.concluida = concluida

    def __str__(self):
        """
        Retorna uma representação amigável da tarefa,
        usada principalmente por print().
        """
        status = "Concluída" if self.concluida else "Pendente"
        return f"Tarefa: {self.descricao} | Status: {status}"

    def __repr__(self):
        """
        Retorna uma representação mais técnica da tarefa,
        útil para depuração e para representar o objeto.
        """
        return (
            f"Tarefa(descricao={self.descricao!r}, "
            f"concluida={self.concluida!r})"
        )


# ============================================================
# Exercício 02
# __eq__ na classe ContaBancaria
# ============================================================

class ContaBancaria:
    def __init__(self, numero, titular, saldo=0.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def __eq__(self, outra):
        """
        Duas contas são consideradas iguais quando
        possuem o mesmo número de conta.
        """
        if not isinstance(outra, ContaBancaria):
            return NotImplemented

        return self.numero == outra.numero

    def __str__(self):
        return (
            f"Conta {self.numero} | "
            f"Titular: {self.titular} | "
            f"Saldo: R$ {self.saldo:.2f}"
        )
