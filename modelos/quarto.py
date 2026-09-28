class Quarto:
    """
    Representa um quarto do hotel.

    Armazena informações básicas como número, tipo,
    capacidade, tarifa e status.
    """

    def __init__(self, numero, tipo, capacidade, tarifa_base):
        self.numero = numero
        self.tipo = tipo
        self.capacidade = capacidade
        self.tarifa_base = tarifa_base
        self.status = "DISPONIVEL"


class QuartoSimples(Quarto):
    """
    Representa um quarto do tipo simples.
    """
    pass


class QuartoDuplo(Quarto):
    """
    Representa um quarto do tipo duplo.
    """
    pass


class QuartoLuxo(Quarto):
    """
    Representa um quarto do tipo luxo.
    """
    pass