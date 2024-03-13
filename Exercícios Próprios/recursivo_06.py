def soma_dos_digitos_quadrados(numero):

    if numero < 10:
        return numero ** 2
    else:
        ultimo_digito = numero % 10
        return ultimo_digito ** 2 +  soma_dos_digitos_quadrados(numero // 10)

numero = int(input())
print(soma_dos_digitos_quadrados(numero))