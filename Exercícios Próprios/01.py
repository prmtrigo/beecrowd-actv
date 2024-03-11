def soma_dos_pares(vetor):
    contador = 0
    for  i in vetor:
        if  i % 2 == 0:
            contador += i
    return contador

vetor = [int(input("Digite um número:")) for i in range(10)]
print(soma_dos_pares(vetor))