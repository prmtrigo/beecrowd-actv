def soma_digitos(numero):
    if numero < 10:
        return numero
    else:
        return numero%10 + soma_digitos(numero//10)

numero = int(input())
print(soma_digitos(numero))