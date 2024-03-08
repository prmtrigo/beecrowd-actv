define_animal_1 = input()
define_animal_2 = input()
define_animal_3 = input()

if define_animal_1 == "vertebrado":
    if define_animal_2 == "ave":
        if define_animal_3 == "carnivoro":
            print ("aguia")
        elif define_animal_3 == "onivoro":
            print("pomba")
    elif define_animal_2 == "mamifero":
        if define_animal_3 == "onivoro":
            print("homem")
        elif define_animal_3 == "herbivoro":
            print("vaca")

elif  define_animal_1 == "invertebrado":
    if define_animal_2 == "inseto":
        if define_animal_3 == "hematofago":
            print("pulga")
        elif define_animal_3 == "herbivoro":
            print("lagarta")
    elif  define_animal_2 == "anelideo":
        if  define_animal_3 == "hematofago":
            print("sanguessuga")
        elif define_animal_3 == "onivoro":
            print("minhoca")