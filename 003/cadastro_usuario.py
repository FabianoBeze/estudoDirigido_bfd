class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def autenticar(self, email, senha):
        if self.email == email and self.senha == senha:
            print(f' Bem vindo {self.nome} Autenticação bem-sucedida!')
            return True
        else:
            print("Falha na autenticação. Email ou senha incorretos.")
            return False      

user = Usuario("Fabiano","fabiano@gmail.com", "1234")

print("=== Sistema de login e Autenticação ===")
em = input("Digite seu email: ")
senh = input("Digite sua senha: ")
user.autenticar(em, senh)