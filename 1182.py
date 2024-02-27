coluna = int(input())

opcao = input()

contador = 0

for i in range(12):
    for j in range(12):
        valor_preenchido = float(input())

        if j == coluna:
            contador += valor_preenchido

if opcao == 'M':
    contador /= 12

print("{:.1f}".format(contador))