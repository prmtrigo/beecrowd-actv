def fibonacci(numero):
    if numero <= 1:
        return numero
    else:
        return fibonacci(numero-1) + fibonacci(numero-2)

numero = int(input())
print(fibonacci(numero))