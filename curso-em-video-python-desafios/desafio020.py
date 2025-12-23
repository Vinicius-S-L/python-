import random

aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
aluno5 = input('Quinto aluno: ')

ordem = [aluno1, aluno2, aluno3, aluno4, aluno5]
random.shuffle(ordem)

print('A ordem de aluno é {}'.format(ordem))

random.shuffle(ordem)
print('Outra ordem de aluno {}'.format(ordem))
