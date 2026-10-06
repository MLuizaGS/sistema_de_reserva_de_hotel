from modelos.hospede import Hospede
from modelos.quarto import Quarto

ORIGENS = ["SITE", "TELEFONE", "BALCAO"]


class Reserva:
    """
    Representa uma reserva de hospedagem.

    Relaciona um hóspede a um quarto durante determinado
    período e mantém informações sobre seu estado,
    pagamentos e adicionais.
    """

    def __init__(self, hospede, quarto, data_entrada, data_saida,
                 quantidade_hospedes, origem="BALCAO"):
        self.hospede = hospede
        self.quarto = quarto
        if data_entrada >= data_saida:
            raise ValueError("A entrada deve ser antes da saída (mínimo 1 noite).")
        self._data_entrada = data_entrada
        self._data_saida = data_saida
        self.origem = origem
        self.status = "PENDENTE"  # toda reserva nasce pendente
        self.pagamentos = []
        self.adicionais = []
                     
    @property
    def data_entrada(self):
        return self._data_entrada

    @data_entrada.setter
    def data_entrada(self, valor):
        if valor >= self._data_saida:
            raise ValueError("A entrada deve ser antes da saída.")
        self._data_entrada = valor

    @property
    def data_saida(self):
        return self._data_saida

    @data_saida.setter
    def data_saida(self, valor):
        if valor <= self._data_entrada:
            raise ValueError("A saída deve ser depois da entrada.")
        self._data_saida = valor

    @property
    def quantidade_hospedes(self):
        return self._quantidade_hospedes

    @quantidade_hospedes.setter
    def quantidade_hospedes(self, valor):
        if valor < 1:
            raise ValueError("Deve haver pelo menos 1 hóspede.")
        if valor > self.quarto.capacidade:
            raise ValueError("Capacidade do quarto excedida.")
        self._quantidade_hospedes = valor

    @property
    def origem(self):
        return self._origem

    @origem.setter
    def origem(self, valor):
        if valor not in ORIGENS:
            raise ValueError(f"Origem inválida. Use uma de {ORIGENS}.")
        self._origem = valor

    @property
    def hospede(self):
        return self._hospede

    @hospede.setter
    def hospede(self, valor):
        if not isinstance(valor, Hospede):
            raise TypeError("hospede deve ser um objeto Hospede.")
        self._hospede = valor

    @property
    def quarto(self):
        return self._quarto

    @quarto.setter
    def quarto(self, valor):
        if not isinstance(valor, Quarto):
            raise TypeError("quarto deve ser um objeto Quarto.")
        self._quarto = valor





