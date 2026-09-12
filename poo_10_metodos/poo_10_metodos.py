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
