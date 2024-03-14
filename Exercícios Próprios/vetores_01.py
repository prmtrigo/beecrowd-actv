notas = []
rodadas = 5

for i in range (rodadas):
    nota = float(input())
    notas.append(nota)

soma = sum(notas)
media = soma / rodadas

print(media)