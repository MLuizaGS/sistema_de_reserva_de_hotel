class Quarto:
    """
    Representa um quarto do hotel.

    Armazena informações básicas como número, tipo,
    capacidade, tarifa e status.
    """
    def __init__(self, numero, tipo, capacidade, tarifa_base, status="DISPONIVEL"):
        self.numero = numero
        self.tipo = tipo
        self.capacidade = capacidade
        self.tarifa_base = tarifa_base
        self.status = status
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        if valor not in TIPOS:
            raise ValueError(f"Tipo inválido. Use um de {TIPOS}.")
        self._tipo = valor

    @property
    def capacidade(self):
        return self._capacidade

    @capacidade.setter
    def capacidade(self, valor):
        if valor < 1:
            raise ValueError("A capacidade deve ser pelo menos 1.")
        self._capacidade = valor

    @property
    def tarifa_base(self):
        return self._tarifa_base

    @tarifa_base.setter
    def tarifa_base(self, valor):
        if valor <= 0:
            raise ValueError("A tarifa base deve ser maior que zero.")
        self._tarifa_base = valor

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, valor):
        if valor not in STATUS:
            raise ValueError(f"Status inválido. Use um de {STATUS}.")
        self._status = valor



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
