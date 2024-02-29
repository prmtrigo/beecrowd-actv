casos_teste = int(input())

numero_total = numero_coelhos = numero_ratos = numero_sapos = 0

for i in range(casos_teste):
    quantidade, animal = input().split()

    quantidade = int(quantidade)

    if animal == 'C':
        numero_coelhos += quantidade
    elif animal == 'R':
        numero_ratos += quantidade
    elif animal == 'S':
        numero_sapos += quantidade

    numero_total += quantidade

porcentagem_coelhos = (numero_coelhos / numero_total) * 100
porcentagem_ratos = (numero_ratos / numero_total) * 100
porcentagem_sapos = (numero_sapos / numero_total) * 100

print("Total: {} cobaias".format(numero_total))
print("Total de coelhos: {}".format(numero_coelhos))
print("Total de ratos: {}".format(numero_ratos))
print("Total de sapos: {}".format(numero_sapos))
print("Percentual de coelhos: {:.2f} %".format(porcentagem_coelhos))
print("Percentual de ratos: {:.2f} %".format(porcentagem_ratos))
print("Percentual de sapos: {:.2f} %".format(porcentagem_sapos))
