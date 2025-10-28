from datetime import date

class Equipamento:
    """
    Representa um equipamento eletrônico.
    """
    def __init__(self, id_equipamento: int, nome: str, descricao: str, data_compra: date, preco: float, id_loja: int):
        """
        Construtor da classe Equipamento.

        Args:
            id_equipamento (int): O identificador único do equipamento.
            nome (str): O nome do equipamento.
            descricao (str): Uma descrição do equipamento.
            data_compra (date): A data em que o equipamento foi comprado.
            preco (float): O preço do equipamento.
            id_loja (int): O ID da loja onde o equipamento foi comprado.
        """
        self.id_equipamento = id_equipamento
        self.nome = nome
        self.descricao = descricao
        self.data_compra = data_compra
        self.preco = preco
        self.id_loja = id_loja

    def __str__(self):
        """
        Retorna uma representação em string do objeto Equipamento.
        """
        return f"Equipamento: {self.nome} (Comprado em: {self.data_compra})"