notas = [100,50,20,10,5]
moedas = [1,0.50,0.25,0.10,0.05,0.01]

valor = float(input())

quantidade_de_moedas = []
quantidade_de_notas = []

for nota in notas:
    quantidade_de_notas = valor // (nota * 100)
    quantidade_de_notas.append(quantidade_de_notas)
    valor -= quantidade_de_notas * nota * 100


for moeda in moedas:
    quantidade_de_moedas = int(valor/moeda)
    quantidade_de_moedas.append(quantidade_de_moedas)
    valor -= (quantidade_de_moedas*moeda)


print("NOTAS:")
for i,nota in enumerate(notas):
    print("{} nota(s) de R$ {:.2f}".format(quantidade_de_notas[i], nota))

print("MOEDAS:")
for i,moeda in enumerate(moedas):
    valor_moeda = moeda/100
    print("{} moedas(s) de R$ {:.2f}".format(quantidade_de_moedas[i], valor_moeda))
