from .pessoa import Pessoa


class Hospede(Pessoa):
    """
    Representa um hóspede do hotel.

    Herda os atributos básicos da classe Pessoa e mantém
    o histórico de reservas realizadas.
    """

    def __init__(self, nome, documento, email, telefone):
        super().__init__(nome, documento, email, telefone)

        self.reservas = []