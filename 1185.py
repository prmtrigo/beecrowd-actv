operacao = input()

soma = 0
contador = 0

for i in range(12):
    for j in range(12):
        valor_matriz = float(input())

        if j < 11 - i:
            soma += valor_matriz
            contador += 1

if operacao  == "M":
    soma /= contador

print("{:.1f}".format(soma))