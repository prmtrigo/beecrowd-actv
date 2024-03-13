def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0

    for i in texto:
        if i in vogais:
            contador += 1
    
    return contador 

texto = input()
print(contar_vogais(texto))