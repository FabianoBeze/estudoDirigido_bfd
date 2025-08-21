"""SOLICITA A IDADE DOS CANDIDATO, SE A IDADE DO CANDIDATO FOR IGUAL OU MAIOR QUE 18 ANOS"""



idade = int(input("Digite sua idade: "))
idade_candidatos = idade

if idade_candidatos >= 18 and 60:
    print("Candidato apto a participar do programa!")
else:
    print("Candidato não pode participar do programa!")