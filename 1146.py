while True:
    senha = int(input())

    if senha == 0:
        break
    
    for i in range(1, senha + 1):
        if(i == senha):
            print(i, end="\n")
        else:
            print(i, end=" ")