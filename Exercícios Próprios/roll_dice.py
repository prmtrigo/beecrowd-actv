import random

def rolagem():
    return random.randint(1,6)

print("---ROLANDO DADOS---")

while True:
    input("Enter para lançar o dado!")

    resultado = rolagem()
    print("O seu resultado foi  {}".format(resultado))
    continuar = input("Deseja lançar o dado novamente? (s/n): ")

    if continuar.lower() != 's':
        break