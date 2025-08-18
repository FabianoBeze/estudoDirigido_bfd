def cadastrar(lista, item):
  lista.append(item)
  print ("Item cadastrado!")

def remover(lista):
    if not lista:
       print("Nenhum item para remover.")
       return
    listar(lista)
    try:
        numero = int(input("Digite o número do item a ser removido: "))
        if 1 <= numero <= len(lista):
            removido = lista.pop(numero -1)
            print(f"Item '{removido}' removido.")
        else:
            print("número não encontrado.")
    except ValueError:
       print("Digite um número válido.")


def listar(lista):
  if not lista:
     print("Lista vazia.")

  else:
    for i, item in enumerate (lista, 1):
       print(f"{i}.{item}")