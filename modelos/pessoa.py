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

    @property
    def nome(self):
        return self._nome
        
    @nome.setter
    def nome(self, valor):
        if not valor or not valor.strip():
            raise ValueError("O nome não pode ser vazio.")
        self._nome = valor.strip()

    @property
    def documento(self):
        return self._documento

    @documento.setter
    def documento(self, valor):
        if not valor or not valor.strip():
            raise ValueError("O documento não pode ser vazio.")
        self._documento = valor.strip()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if "@" not in valor or "." not in valor:
            raise ValueError("E-mail inválido.")
        self._email = valor

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, valor):
        if not valor or not valor.strip():
            raise ValueError("O telefone não pode ser vazio.")
        self._telefone = valor.strip()


