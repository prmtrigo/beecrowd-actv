posicao = int(input())

termo_anterior = 0
termo_seguinte = 1

for i in range(posicao):

    if i == posicao-1:
        print(termo_anterior)

    else:
        print(termo_anterior, end=" ")
    
    termo_anterior,termo_seguinte = termo_seguinte,termo_anterior + termo_seguinte
