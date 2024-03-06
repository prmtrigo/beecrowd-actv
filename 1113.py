while True:
    numero_inicio, numero_fim = map(int, input().split())

    if numero_inicio == numero_fim:
        break

    if numero_inicio > numero_fim:
        print("Decrescente")

    else:
        print("Crescente")