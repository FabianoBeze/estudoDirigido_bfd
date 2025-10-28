from datetime import date

class Garantia:
    """
    Representa a garantia de um equipamento.
    """
    def __init__(self, id_garantia: int, id_equipamento: int, data_vencimento: date, documento_fiscal_path: str, seguradora: str):
        """
        Construtor da classe Garantia.

        Args:
            id_garantia (int): O identificador único da garantia.
            id_equipamento (int): O ID do equipamento associado a esta garantia.
            data_vencimento (date): A data de vencimento da garantia.
            documento_fiscal_path (str): O caminho para o arquivo do documento fiscal.
            seguradora (str): O nome da seguradora, se houver.
        """
        self.id_garantia = id_garantia
        self.id_equipamento = id_equipamento
        self.data_vencimento = data_vencimento
        self.documento_fiscal_path = documento_fiscal_path
        self.seguradora = seguradora

    def __str__(self):
        """
        Retorna uma representação em string do objeto Garantia.
        """
        return f"Garantia (ID: {self.id_garantia}) - Vence em: {self.data_vencimento}"