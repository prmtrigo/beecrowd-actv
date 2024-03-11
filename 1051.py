def calcular_imposto_renda(salario):
    if salario <= 2000:
        return 0
    elif salario <= 3000:
        return (salario - 2000) * 0.08
    elif salario <= 4500:
        return calcular_imposto_renda(3000) + (salario - 3000) * 0.18
    else:
        return calcular_imposto_renda(4500) + (salario - 4500) * 0.28

salario = float(input())
imposto = calcular_imposto_renda(salario)

if imposto == 0:
    print("Isento")
else:
    print("R$ {:.2f}".format(imposto))
