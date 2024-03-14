tamanho = int(input())
estoque = []

for i in range (tamanho):
    quantidade = int(input())
    estoque.append(quantidade)

contador = 0

for i in estoque:
    contador += i

print(contador)
