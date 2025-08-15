#funcoes.py
def exibir_menu():
    print("\n[1] - Cadastrar item [2] - Listar itens [0] - Sair")

def cadastrar(itens):
    nome = input("Digite o nome do item: ").strip()
    if not nome:
        print("x Nome não pode ser vazio.")
        return
    if nome in itens:
        print("x Item já cadastrado.")
        return
    itens.append(nome)
    print(" Item cadastrado com sucesso!")

def listar(itens):
    if not itens:
        print("x Nenhum item cadastrado.")
    else:
      for i, item in enumerate(itens, start= 1):
        print(f"{i} - {item}")