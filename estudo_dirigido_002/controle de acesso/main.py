'''Desafio:
Ler nome e idade de 5 pessoas.
Verificar se são maiores de idade.
Mostrar o total de aprovados e recusados.
Regras:
Usar funções para cada parte (entrada, verificação, contagem).
Exibir resumo no final com contagem de maiores e menores de idade.
Dica:
Separar responsabilidades: ler_pessoa() , verificar_idade() , acumular_resultados() , mostrar_resumo() '''
from fun import*

def main():
    for _ in range(5):
        ler_pessoa()
    for nome, idade in pessoas.items():
        if idade >= 18:
            resultado = (True, "")
        else:
            resultado = (False, "Menor de idade")
        acumular_resultados(acumulado, resultado)
    mostrar_resumo(acumulado)

if __name__ == '__main__':
    main()