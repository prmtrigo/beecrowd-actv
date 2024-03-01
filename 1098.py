i = 0
j = 1
valor = 0
auxiliar1 = 0
auxiliar2 = 0

while (i <= 2):
    if(auxiliar2 == 0):
        print("I={:.0f} J={:.0f}".format(i, j))
    else:
        print("I={:.1f} J={:.1f}".format(i, j))

    auxiliar1 += 1
    if (auxiliar1 == 3):
        i += 0.2
        valor += 0.2
        j = valor
        auxiliar1 = 0
        auxiliar2 += 1

    if (auxiliar2 == 5):
        auxiliar2 = 0
    j += 1
