while True:
    numero = int(input())

    if numero == 0:
        break

    matriz = []
    for i in range(numero):
        linha = [str(2 ** (i + j)) for j in range(numero)]
        matriz.append(linha)

    maior_numero = len(matriz[-1][-1])

    for linha in matriz:
        for j in range(numero):
            while len(linha[j]) < maior_numero:
                linha[j] = ' ' + linha[j]
        print(' '.join(linha))

    print()
