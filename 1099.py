casos_teste = int(input())

for i in range(casos_teste):
    inicio,fim = list(map(int, input().split()))
    contador = 0

    if(inicio == fim):
        print(0)
    else:
        auxiliar1 = 0

        if(inicio > fim):
            auxiliar1 = inicio
            inicio = fim
            fim = auxiliar1
        
        while(inicio < (fim -1)):
            inicio +=1

            if(inicio %2 != 0):
                contador +=inicio
        
        print(contador)
