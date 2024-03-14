def buscar_temperatura (temperaturas, achar_temperatura):
    if(achar_temperatura in temperaturas):
        print("Temperatura encontrada")

    else:
        print("Temperatura não encontrada")

tamanho = int(input())
temperaturas = []

for i in range (tamanho):
    temperatura = float(input())
    temperaturas.append(temperatura)

achar_temperatura = int(input())

buscar_temperatura(temperaturas, achar_temperatura)