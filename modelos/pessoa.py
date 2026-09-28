class Pessoa:
    """
    Classe base que representa uma pessoa no sistema do hotel.

    Contém os dados básicos que poderão ser utilizados
    pelas classes derivadas.
    """

    def __init__(self, nome, documento, email, telefone):
        self.nome = nome
        self.documento = documento
        self.email = email
        self.telefone = telefone