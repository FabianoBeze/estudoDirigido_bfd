from datetime import date

class Garantia:
    """
    Representa a garantia de um equipamento.
    """
    def __init__(self, id_garantia: int, id_equipamento: int, data_inicio: date, data_fim: date, tipo: str):
        """
        Construtor da classe Garantia.

        Args:
            id_garantia (int): O identificador único da garantia.
            id_equipamento (int): O ID do equipamento associado a esta garantia.
            data_inicio (date): A data de início da garantia.
            data_fim (date): A data de vencimento da garantia.
            tipo (str): O tipo de garantia (ex: 'Padrão', 'Estendida').
        """
        self.id_garantia = id_garantia
        self.id_equipamento = id_equipamento
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.tipo = tipo

    def __str__(self):
        """
        Retorna uma representação em string do objeto Garantia.
        """
        return f"Garantia (ID: {self.id_garantia}) - Vence em: {self.data_fim}"