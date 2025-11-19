class Funcionario:
    """Representa um funcionário com nome, cargo e salário."""
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        print(f"Funcionário '{self.nome}' ({self.cargo}) contratado com salário de R${self.salario:.2f}.")

    def aumentar_salario(self, percentual):
        """
        Aumenta o salário do funcionário com base em um percentual.
        A lógica do cálculo fica encapsulada aqui dentro.
        """
        if percentual <= 0:
            print("O percentual de aumento deve ser um valor positivo.")
            return

        aumento = self.salario * (percentual / 100)
        self.salario += aumento
        
        print(f"\nSalário de '{self.nome}' aumentado em {percentual}%.")
        print(f"Novo salário: R${self.salario:.2f}.")

    def mostrar_detalhes(self):
        """Exibe os detalhes atuais do funcionário."""
        print(f"\n--- Detalhes do Funcionário ---")
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário: R${self.salario:.2f}")
        print("-----------------------------")


# --- Exemplo de Uso ---

# 1. Criar uma instância da classe Funcionario.
func1 = Funcionario("Carlos Silva", "Desenvolvedor Sênior", 7500.00)

# 2. Mostrar os detalhes iniciais.
func1.mostrar_detalhes()

# 3. Usar o método encapsulado para dar um aumento.
#    Note que não precisamos saber a fórmula do cálculo aqui fora,
#    apenas chamamos o método e passamos o percentual.
func1.aumentar_salario(10)

# 4. Mostrar os detalhes novamente para ver o salário atualizado.
func1.mostrar_detalhes()

# 5. Tentar usar um valor inválido.
func1.aumentar_salario(-5)