from funcoes import cadastrar,listar,remover
itens = []

while True:
  print("=== Cadastro de itens BFD ===\nDigite:")  
  print("[1] Cadastrar " "\n" "[2] Listar" "\n" "[3] Remover" "\n" "[0] Sair") 
  op = input("Escolha: ").strip()

  if op == "1":
     nome = input("item: ").strip()
     if nome in itens:
        print("Item já cadastrado.\nfavor cadastrar próximo item: ")
     else:  
      cadastrar(itens, nome)

  elif op == "2":
     print("Lista de produtos:")
     listar(itens)
  
  elif op == "3":
     remover(itens)

  elif op == "0":
     break
  
  else:
     print("Opção inválida.")