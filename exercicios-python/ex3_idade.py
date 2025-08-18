idade = int(input("Digite sua idade: "))
cidade = input("Digite sua cidade: ")
if idade >= 60:
    print("Você é um idoso e mora em", cidade) 
elif idade >= 18:
    print("Você é um adulto e mora em", cidade)
else:
    print("Você é uma criança e mora em", cidade)