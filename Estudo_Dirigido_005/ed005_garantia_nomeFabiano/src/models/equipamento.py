from datetime import date

class Equipamento:
    """
    Representa um equipamento eletrônico.
    """
    def __init__(self, id_equipamento: int, nome: str, preco: float, data_venda: date, id_loja: int):
        """
        Construtor da classe Equipamento.

        Args:
            id_equipamento (int): O identificador único do equipamento.
            nome (str): O nome do equipamento.
            preco (float): O preço do equipamento.
            data_venda (date): A data em que o equipamento foi vendido.
            id_loja (int): O ID da loja onde o equipamento foi comprado.
        """
        self.id_equipamento = id_equipamento
        self.nome = nome
        self.preco = preco
        self.data_venda = data_venda
        self.id_loja = id_loja

    def __str__(self):
        """
        Retorna uma representação em string do objeto Equipamento.
        """
        return f"Equipamento: {self.nome} (Vendido em: {self.data_venda})"