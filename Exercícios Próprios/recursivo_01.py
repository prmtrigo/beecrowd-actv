def soma_recursiva(numero):
    if numero == 1:
        return 1
    else:
        return numero + soma_recursiva(numero - 1)

numero = int(input())
print(soma_recursiva(numero))