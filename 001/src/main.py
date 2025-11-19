#main.py

from funcoes import exibir_menu, cadastrar, listar

def main():
    itens = []
    print("===App de Itens(BFD 2.0)=== ")
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            cadastrar(itens)
        elif opcao == '2':
            listar(itens)
        elif opcao == '0':
            print("Saindo do aplicativo...")
            break
        else:
            print("x Opção inválida. Tente novamente.")
if __name__ == "__main__":
    main()