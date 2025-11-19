class Usuario:
    """Representa um usuário com nome e saldo."""
    def __init__(self, nome, saldo_inicial=0):
        self.nome = nome
        self.saldo = saldo_inicial
        print(f"Usuário '{self.nome}' criado com saldo de R${self.saldo:.2f}.")

    def adicionar_saldo(self, valor):
        """Adiciona um valor ao saldo do usuário."""
        if valor > 0:
            self.saldo += valor
            print(f"Saldo de '{self.nome}' atualizado para R${self.saldo:.2f}.")
        else:
            print("O valor para adicionar ao saldo deve ser positivo.")

    def mostrar_saldo(self):
        """Exibe o saldo atual do usuário."""
        print(f"Saldo atual de '{self.nome}': R${self.saldo:.2f}.")


class Pagamento:
    """Representa uma transação de pagamento para um usuário."""
    def __init__(self, usuario, valor):
        if not isinstance(usuario, Usuario):
            raise TypeError("O pagamento deve estar associado a um objeto Usuario.")
        
        self.usuario = usuario
        self.valor = valor
        self.status = "Pendente"
        print(f"Pagamento de R${self.valor:.2f} criado para '{self.usuario.nome}'. Status: {self.status}.")

    def processar(self):
        """Processa o pagamento, adicionando o saldo ao usuário se o valor for válido."""
        print(f"\nProcessando pagamento de R${self.valor:.2f} para '{self.usuario.nome}'...")
        if self.valor > 0:
            self.usuario.adicionar_saldo(self.valor)
            self.status = "Aprovado"
            print(f"Pagamento processado com sucesso! Status: {self.status}.")
        else:
            self.status = "Recusado"
            print(f"Valor de pagamento inválido. Status: {self.status}.")


# --- Exemplo de Uso da Interação entre Classes ---

# 1. Crie uma instância de Usuario.
usuario_vip = Usuario("Ana", 100)
usuario_vip.mostrar_saldo()

# 2. Crie uma instância de Pagamento, associando-a ao usuário.
pagamento_fatura = Pagamento(usuario_vip, 250)

# 3. Chame o método para processar o pagamento.
#    Este método dentro da classe Pagamento irá chamar o método adicionar_saldo do objeto usuario_vip.
pagamento_fatura.processar()

# 4. Verifique o saldo do usuário novamente para confirmar que foi atualizado.
usuario_vip.mostrar_saldo()