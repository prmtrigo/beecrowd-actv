valor = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]

print(valor)

for nota in notas:
    quantidade = valor // nota
    valor %= nota
    print("{} nota(s) de R$ {:.2f} ".format(quantidade, nota).replace('.', ','))

