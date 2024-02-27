salario = float(input())

novo_salario = 0.0
valor_ganho = 0.0
aumento_percentual = 0.0

if salario <= 400.00:
    aumento_percentual = 15
elif salario <= 800.00:
    aumento_percentual = 12
elif salario <= 1200.00:
    aumento_percentual = 10
elif salario <= 2000.00:
    aumento_percentual = 7
else:
    aumento_percentual = 4

valor_aumento = salario * (aumento_percentual / 100)
novo_salario = salario + valor_aumento

valor_ganho = valor_aumento

print("Novo salario: {:.2f}".format(novo_salario))
print("Reajuste ganho: {:.2f}".format(valor_ganho))
print("Em percentual: {} %".format(int(aumento_percentual)))
