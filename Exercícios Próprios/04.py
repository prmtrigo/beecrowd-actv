def verifica_palindromo(texto):

    return texto == texto[::-1]

texto = input("Digite uma string: ")
print(verifica_palindromo(texto))
