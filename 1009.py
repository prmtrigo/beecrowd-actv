nome = input()
salario = float(input())
vendas = float(input())

bonus = vendas * 0.15

salario_final = bonus + salario

print("TOTAL = R$ {:.2f}".format(salario_final))