posicao = int(input())

fatorial = 1
contador = 1

while contador < posicao+1:
    fatorial *= contador
    contador += 1

print(fatorial)