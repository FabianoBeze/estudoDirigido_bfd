class Documentos:
    """
    Representa um documento fiscal (nota fiscal).
    """
    def __init__(self, id_doc: int, numero_nota: str):
        """
        Construtor da classe Documentos.

        Args:
            id_doc (int): O identificador único do documento.
            numero_nota (str): O número da nota fiscal.
        """
        self.id_doc = id_doc
        self.numero_nota = numero_nota

    def __str__(self):
        """
        Retorna uma representação em string do objeto Documentos.
        """
        return f"Documento (ID: {self.id_doc}) - Nota: {self.numero_nota}"