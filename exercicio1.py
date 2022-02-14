# O código ficará em repetição até o usuário decidir não continuar
while (True):
    print("Nome do aluno: ")
    nome = input()

    print("Idade:")
    idade = input()
    idade = int(idade)

    # Classifica o aluno de acordo com sua idade
    if 1 <= idade <= 5:
        print("Educação Infantil")
    elif 6 <= idade <= 10:
        print("Ensino Fundamental I")
    elif 11 <= idade <= 14:
        print("Ensino Fundamental II")
    elif idade >= 15:
        print("Ensino Médio")
    else:
        print("Sem classificação")

    print("Deseja continuar? (s/n)")
    continuar = input()

    if continuar != "s":
        break