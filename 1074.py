casos_teste = int(input())

for i in range(casos_teste):

    numero = int(input())

    if numero > 0:
        if numero  % 2 == 0:
            print("EVEN POSITIVE")
        else:
            print("ODD POSITIVE")
    
    elif numero < 0:
        if numero  % 2 == 0:
            print("EVEN NEGATIVE")
        else:
            print("ODD NEGATIVE")
    
    if numero == 0:
        print("NULL")