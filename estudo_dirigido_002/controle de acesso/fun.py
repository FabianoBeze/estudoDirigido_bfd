'''Separar responsabilidades: ler_pessoa() , verificar_idade() , acumular_resultados() , mostrar_resumo()'''
pessoas = {}
acumulado = {'aprovados': 0, 'recusados': 0, 'motivo': ''}
maior_idade = []
menor_idade = []
def ler_pessoa():
    nome = input('Digite o nome: ')
    idade = []
    idad = int(input('Digite a idade: '))
    #idade.append(idad)
    pessoas[nome] = idad
    print(pessoas)

def verificar_idade():
    for nome, idad in pessoas.items():
        if idad >= 18:
            resultado = "Maior idade"
            maior_idade.append(nome)
        else:
            resultado = "Menor de idade"
            menor_idade.append(nome)
        print(f"===Verificando===\n{nome}: {resultado}")
    print(maior_idade)
    print(menor_idade)
def acumular_resultados(acumulado, resultado):  
    if resultado[0]:
        acumulado['aprovados'] += 1
    else:
        acumulado['recusados'] += 1
        acumulado['motivo'] += resultado[1] + '\n'  # Adiciona o motivo ao acumulado  
        return acumulado 
    return acumulado
def mostrar_resumo(acumulado):
    print(f'Total de aprovados: {acumulado["aprovados"]}')
    print(f'Total de recusados: {acumulado["recusados"]}')
    print(f'Motivos dos recusados:\n{acumulado["motivo"]}')