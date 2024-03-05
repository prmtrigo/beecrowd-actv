inicio = int(input())
final = int(input())

if inicio > final:
    inicio,final =  final,inicio

contador = 0

for i in range (inicio,final +1):
    if i % 13 != 0:
        contador += i

print(contador)