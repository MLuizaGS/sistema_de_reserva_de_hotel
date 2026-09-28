class Pagamento:
    """
    Representa um pagamento relacionado a uma reserva.
    """

    def __init__(self, data, forma, valor):
        self.data = data
        self.forma = forma
        self.valor = valor