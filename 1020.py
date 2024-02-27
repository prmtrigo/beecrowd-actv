idade_em_dias = int(input())

anos = idade_em_dias // 365
dias_restantes = idade_em_dias %365
meses = dias_restantes // 30
dias = dias_restantes %30

print(anos, "ano(s)")
print(meses, "mes(es)")
print(dias, "dia(s)")