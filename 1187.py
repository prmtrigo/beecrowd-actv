operacao = input()

soma = 0
contador_elementos = 0

for i in range(12):
    for j in range(12):
        valor = float(input())
        
        if i < j and i + j < 11:
            soma += valor
            contador_elementos += 1

if operacao == 'M':
    soma /= 30.0

print("{:.1f}".format(soma))