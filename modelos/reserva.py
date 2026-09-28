class Reserva:
    """
    Representa uma reserva de hospedagem.

    Relaciona um hóspede a um quarto durante determinado
    período e mantém informações sobre seu estado,
    pagamentos e adicionais.
    """

    def __init__(
        self,
        hospede,
        quarto,
        data_entrada,
        data_saida,
        quantidade_hospedes,
        origem
    ):
        self.hospede = hospede
        self.quarto = quarto
        self.data_entrada = data_entrada
        self.data_saida = data_saida
        self.quantidade_hospedes = quantidade_hospedes
        self.origem = origem
        self.status = "PENDENTE"

        self.pagamentos = []
        self.adicionais = []