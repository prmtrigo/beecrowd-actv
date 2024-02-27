id_funcionario = int(input())
horas_trabalhadas = int(input())
ganho_hora = float(input())

salario_base = horas_trabalhadas * ganho_hora

print("NUMBER =", id_funcionario)
print("SALARY = U$ {:.2f}".format(salario_base))