#Separar responsabilidades: entrada, processamento e saída.


nome = {}

def ler_dados():
 for i in range(5):
  name = input("Digite seu nome: ")
  idade = []
  idad = int(input("Digite sua idade: "))
  idade.append(idad)
  nome[name] = idade 
   
def verificar_idade():  
  for i in nome:
    if nome[i][0] >= 18:
      resultado = "Maior idade"
    else:
      resultado = "Menor de idade"
    print(f"===Verificando===\n{i}: {resultado}")

def exibir_resultado():
  return verificar_idade
  
  
