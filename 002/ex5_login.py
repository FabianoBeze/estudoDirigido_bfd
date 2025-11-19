# aplicativo de senha com 3 tentativa e bloqueia.


'''senha_correta = "python123"
tentativa = ""
contador = 0
while tentativa != senha_correta and contador < 3:
    tentativa = input("Digite a senha: ")
    if tentativa == senha_correta:
        print("Acesso permitido!")
    else:
        contador += 1
        if contador < 3:
            print("Senha incorreta, tente novamente.")  
        else:
            print("Acesso Bloqueado!")'''
senha=0
nova_senha =""
print("Crie sua senha:")
senha = input("Digite sua senha: ")
nova_senha = senha
print("Senha criada com sucesso!")

tentativa = ""
contador = 0
while tentativa != nova_senha and contador < 3:
    tentativa = input("Digite sua senha para acessar: ")
    if tentativa == nova_senha:
        print("Acesso permitido!\nBem-vindo ao sistema!")
    else:
        contador += 1
        if contador < 3:
            print("Senha incorreta, tente novamente.")  
        else:
            print("Acesso Bloqueado!")
            

      
    
        

