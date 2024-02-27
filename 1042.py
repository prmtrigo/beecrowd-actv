numero_1,numero_2,numero_3 = map(int, input().split())

valores = [numero_1, numero_2, numero_3]

valores_ordenados = sorted(valores)

for valor in valores_ordenados:
    print(valor)

print()

for valor in valores:
    print(valor)