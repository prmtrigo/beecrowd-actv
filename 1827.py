while True:
    try:
        tamanho_matriz = int(input())
        inicio = tamanho_matriz // 3
        fim = tamanho_matriz - inicio

        matriz = [[0 for _ in range(tamanho_matriz)] for _ in range(tamanho_matriz)]

        for i in range(tamanho_matriz):
            matriz[i][i] = 2

        j = 0
        for i in range(tamanho_matriz - 1, -1, -1):
            matriz[j][i] = 3
            j += 1

        for i in range(inicio, fim):
            for j in range(inicio, fim):
                matriz[i][j] = 1

        matriz[tamanho_matriz // 2][tamanho_matriz // 2] = 4

        for linha in matriz:
            print(''.join(map(str, linha)))
        print()

    except EOFError:
        break
