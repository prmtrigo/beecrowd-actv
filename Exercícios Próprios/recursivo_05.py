def fatorial(numero):
    if numero == 0 or numero == 0:
        return 1
    else:
        return numero * fatorial(numero-1)

numero = int(input())
print(fatorial(numero))