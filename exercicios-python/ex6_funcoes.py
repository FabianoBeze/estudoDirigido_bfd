# crie uma função idade, que retorne quantos anos faltam para 100:  
'''def saudacao(nome):
  return f"Olá, {nome}"

usuario = input("Digite seu nome: ")
print(saudacao (usuario))'''


def idade_para_100(idade):
    restante = 100 - idade
    return f"Faltam, {restante} anos para completar 100 anos."

new_idade = int(input("Digite sua idade: "))

print(idade_para_100(new_idade))