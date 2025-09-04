alunos = {}
notas=[]
medias= []
def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    notas = []
    for i in range(4):
        nota = float(input(f"Digite a {i+1}ª nota do aluno: "))
        notas.append(nota)
    alunos[nome] = notas
    print(f"Aluno {nome} adicionado com notas {notas}.")

def media_aluno():
    nome = input("Digite o nome do aluno para ver a média: ")
    if nome in alunos:
        notas = alunos[nome]
        media = sum(notas) / len(notas)
        if media >= 7:
            print(f"Média de {nome}: {media:.2f} Aprovado!!!")
        else:
            print(f"Média de {nome}: {media:.2f} Reprovado!!!")
        
        return media
    else:
        print("Aluno não encontrado.")
        return None

def listar_medias():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for nome, notas in alunos.items():
            media = sum(notas) / len(notas)
            if media >= 7:
                print(f"Aluno: {nome}: Média {media:.2f}: Aluno Aprovado!!!")
            else:
                print(f"Aluno: {nome}: Média {media:.2f}: !!!Reprovado!!!")
            