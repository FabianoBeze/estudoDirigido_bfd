#Criar uma função somar(a, b) que retorna a soma de dois números.
'''def somar(a, b):
 return a + b
resultado = somar(5, 3)
print("Resultado:", resultado)'''

#Expansão 1 (5 min): Tornar interativo com input()  
'''def somar(a, b):
 return a + b
resultado = somar(5, 3)
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
print("A soma é:", somar(a, b))'''

#Expansão 2 (10 min): Adaptar a função para somar todos os elementos de uma lista.
def somar_lista(numeros):
  return sum(numeros)

numeros = []
for i in range (5):  
  numero = int(input("Digite um número: "))
  numero=numeros.append(numero)
  print(numeros)
  print(f'A soma dos números é: {somar_lista(numeros)}')