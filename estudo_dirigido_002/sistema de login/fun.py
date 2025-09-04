senha = "1234"
tentativas = []
def solicitar_login():
  tentativa = (input("Digite a senha: "))
  tentativas.append(tentativa)
  
def verificar_login():
  contador = 0
  while contador < 3:
    contador += 1
    solicitar_login()
    if tentativas [-1] == senha:  # Verifica a última tentativa
      print("Bem vindo!!!")
      break
    else:
      print("Senha incorreta") 
      if contador == 3:
        print("Acesso bloqueado!")