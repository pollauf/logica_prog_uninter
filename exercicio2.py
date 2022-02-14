print("Digite um nome:")
nome = input()

# Transforma o nome em letras maiúsculas
nome = nome.upper()

# Substitui as vogais pelos respectivos caracteres especiais
nome = nome.replace('A', '@')
nome = nome.replace('E', '&')
nome = nome.replace('I', '!')
nome = nome.replace('O', '#')
nome = nome.replace('U', '*')

print(nome)