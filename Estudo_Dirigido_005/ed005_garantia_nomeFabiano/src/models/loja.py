class Loja:
    """
    Representa uma loja onde os equipamentos são comprados.
    """
    def __init__(self, id_loja: int, nome: str, endereco: str):
        """
        Construtor da classe Loja.

        Args:
            id_loja (int): O identificador único da loja.
            nome (str): O nome da loja.
            endereco (str): O endereço da loja.
        """
        self.id_loja = id_loja
        self.nome = nome
        self.endereco = endereco

    def __str__(self):
        """
        Retorna uma representação em string do objeto Loja.
        """
        return f"Loja: {self.nome} (ID: {self.id_loja})"