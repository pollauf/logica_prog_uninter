from random import randint

# Lista que guardará as inscrições
inscricoes = []

while(True):
    # Exibição e seleção de opção
    print('\n1 - Nova inscrição')
    print('2 - Ver inscrições')
    print('3 - Encerrar')

    opcao = input('Opção: ')
    opcao = int(opcao)

    if opcao == 1:
        # Voucher gerado automaticamente
        voucher = randint(100, 400)

        print('\nVoucher:', voucher)
        nome = input('Nome: ')
        email = input('E-mail: ')
        telefone = input('Telefone: ')
        curso = input('Curso: ')

        # Dicionário da inscrição
        inscricao = {
            'voucher': voucher,
            'nome': nome,
            'email': email,
            'telefone': telefone,
            'curso': curso
        }

        # Inclusão da inscrição na lista
        inscricoes.append(inscricao)
    elif opcao == 2:
        # Iteração e exibição das inscrições, caso houver
        if len(inscricoes) > 0:
            for inscricao in inscricoes:
                print('\n###################')
                print('Voucher:', inscricao['voucher'])
                print('Nome:', inscricao['nome'])
                print('E-mail:', inscricao['email'])
                print('Telefone:', inscricao['telefone'])
                print('Curso:', inscricao['curso'])
                print('###################')
        else:
            print('Não há inscrições!')
    elif opcao == 3:
        print('Encerrado')
        break
    else:
        print('Opção inválida!')