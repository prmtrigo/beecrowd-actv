def maior_numero(vetor):
    maior_numero = 0

    for i in  range(len(vetor)):
        if vetor[i] > maior_numero:
            maior_numero = vetor[i]
    
    return maior_numero

vetor = [int(input("Digite um número:")) for i in range(5)]
print(maior_numero(vetor))