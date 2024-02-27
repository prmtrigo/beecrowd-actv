nota_1, nota_2,nota_3,nota_4 = map(float, input().split())

media_das_notas = (nota_1 * 2 + nota_2 * 3 + nota_3 * 4 + nota_4 * 1) /10

print("Media: {:.1f}".format(media_das_notas))

if media_das_notas < 5.0:
    print("Aluno reprovado.")
elif media_das_notas >= 7.0:
    print("Aluno aprovado.")
else:
    print("Aluno em exame.")

    # ao estar em exame, o aluno precisa fazer um novo exame
    # média entre a média e a nova nota do exame

    nota_do_exame = float(input())

    print("Nota do exame: {:.1f}".format(nota_do_exame))

    nova_media = (media_das_notas + nota_do_exame)/2

    if nova_media < 5.0:
        print("Aluno reprovado.")
    else:
        print("Aluno aprovado.")

    print("Media final: {:.1f}".format(nova_media))