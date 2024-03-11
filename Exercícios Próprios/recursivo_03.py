def inverter_string(texto):
    if len(texto) == 0:
        return texto
    else:
        return texto[-1] + inverter_string(texto[:-1])

texto = input()
print(inverter_string(texto))