# Valida a compatibilidade dos animais vizinhos informados em uma lista
def validarAnimaisVizinhos(animaisVizinhos):
    if 'R' in animaisVizinhos and 'G' in animaisVizinhos:
        return False
    elif 'C' in animaisVizinhos and 'O' in animaisVizinhos:
        return False
    elif 'G' in animaisVizinhos and 'C' in animaisVizinhos:
        return False
    elif 'Q' in animaisVizinhos and 'R' in animaisVizinhos:
        return False

    return True


def verificaCompatibilidadeAnimais(quartos):
    # Percorre todos os animais nos quartos comparando os vizinhos da horizontal
    for x in range(2):
        animalAtual = ''
        animalAnterior = ''

        for y in range(4):
            animalAtual = quartos[x][y]

            animaisVizinhos = [animalAtual, animalAnterior]

            # Se os animais forem incompatíveis, retorna-se False
            if not validarAnimaisVizinhos(animaisVizinhos):
                return False
            else:
                animalAnterior = animalAtual

    # Percorre todos os animais nos quartos comparando os vizinhos da vertical
    for x in range(4):
        animaisVizinhos = [quartos[0][x], quartos[1][x]]

        # Se os animais forem incompatíveis, retorna-se False
        if not validarAnimaisVizinhos(animaisVizinhos):
            return False
        else:
            animalAnterior = animalAtual

    return True


def alocarAnimal(quartos, animal, posicao):
    # Verifica se a posição é válida
    if not (1 <= posicao <= 8):
        return False

    indexLista = 0
    valorSubtrairIndex = 1

    # Se a posição for maior que 4, a alocação deve ser feita na segunda lista
    if posicao > 4:
        indexLista = 1
        valorSubtrairIndex = 5

    # Verifica se o quarto está disponível e faz a alocação
    if quartos[indexLista][posicao - valorSubtrairIndex] == '-':
        quartos[indexLista][posicao - valorSubtrairIndex] = animal
    else:
        return False

    return quartos


# Dicionário para facilitar o enunciado das fases apresentando o nome do mesmo considerando as siglas dos animais
dicionarioAnimais = {
    'G': 'Gato',
    'C': 'Cão',
    'R': 'Rato',
    'O': 'Osso',
    'Q': 'Queijo',
}

# Lista das listas de animais para alocar em cada fase
animaisFases = [
    ['R', 'G'],
    ['C', 'C', 'O'],
    ['G', 'R', 'O'],
    ['Q', 'Q', 'O']
]

# Listas das listas de quartos e sua pré-distribuição em cada fase
quartos = [
    [
        ['*', '*', '-', 'G'],
        ['R', '-', '*', '*']
    ],
    [
        ['-', '*', '*', '*'],
        ['*', 'C', '-', '-']
    ],
    [
        ['-', '*', '*', '*'],
        ['-', 'G', '-', '*']
    ],
    [
        ['-', '-', '-', '*'],
        ['*', 'R', '*', '*']
    ]
]

print("######## HOTEL DOS ANIMAIS ########")

# Percorre todas as fases e gera um texto informando a objetivo da mesma
for fase in range(4):
    print('\nFase: ', fase + 1)

    # Gera o texto da disponibilidade dos quartos
    quarto = quartos[fase]

    vagasQuartos = '|'

    for vagaQuarto in quarto[0]:
        vagasQuartos += ' ' + vagaQuarto + ' |'

    vagasQuartos += '\n|'

    for vagaQuarto in quarto[1]:
        vagasQuartos += ' ' + vagaQuarto + ' |'

    print('Quartos:')
    print(vagasQuartos)

    # Gera o texto dos animais a serem alocados
    animaisAlocarInfo = ''

    for animal in animaisFases[fase]:
        animaisAlocarInfo += dicionarioAnimais[animal] + '  '

    print('Você deve alocar:', animaisAlocarInfo)

    sucessoAlocacao = True

    # Solicita a alocação de cada animal
    for animal in animaisFases[fase]:
        print('Posição de 1-8 para alocar', dicionarioAnimais[animal], ':')
        posicao = input()
        posicao = int(posicao)

        quarto = alocarAnimal(quarto, animal, posicao)

        if not quarto:
            sucessoAlocacao = False
            break

    # Verifica-se se os animais foram alocados em quartos não ocupados e a compatibilidade dos mesmos
    if not sucessoAlocacao or not verificaCompatibilidadeAnimais(quarto):
        print('Game Over!!!')
        break
