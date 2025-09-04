import notas

def main():
    while True:
        print("\n==== Controle de Notas ====")
        print("1 - Adicionar aluno e suas notas")
        print("2 - Mostrar média de um aluno")
        print("3 - Listar médias")
        print("4 - Sair")

        opcao = input("Digite uma opção: ")

        if opcao == "1":
            notas.adicionar_aluno()

        elif opcao == "2":
            notas.media_aluno()

        elif opcao == "3":
            notas.listar_medias()

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()