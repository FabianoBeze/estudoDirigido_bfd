class Usuarios:
    """
    Representa um usuário do sistema.
    """
    def __init__(self, id_usuario: int, cpf_usuario: str):
        """
        Construtor da classe Usuarios.

        Args:
            id_usuario (int): O identificador único do usuário.
            cpf_usuario (str): O CPF do usuário.
        """
        self.id_usuario = id_usuario
        self.cpf_usuario = cpf_usuario

    def __str__(self):
        """
        Retorna uma representação em string do objeto Usuarios.
        """
        return f"Usuário (ID: {self.id_usuario}) - CPF: {self.cpf_usuario}"