def media_numero(vetor):
    acumulador = 0

    media = sum(vetor)/len(vetor)

    return media

vetor = [int(input("Digite um número:")) for i in range(5)]
print(media_numero(vetor))