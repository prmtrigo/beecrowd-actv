tamanho = int(input())

valores = [int(x) for x in input().split()]

menor_valor = valores[0]
posicao_menor = 0

for i in range(1, tamanho):
    if valores[i] < menor_valor:
        menor_valor = valores[i]
        posicao_menor = i

print("Menor valor:", menor_valor)
print("Posicao:", posicao_menor)
