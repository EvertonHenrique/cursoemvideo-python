from random import choice, randint, shuffle
aluno1 = str(input('Primeiro Aluno: '))
aluno2 = str(input('Segundo Aluno: '))
aluno3 = str(input('Terceiro Aluno: '))
aluno4 = str(input('Quarto Aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print(f'A ordem de escolha foi {lista}')