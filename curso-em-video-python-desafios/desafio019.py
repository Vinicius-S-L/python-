import random
while True:
    nome1 = input('Digite o nome do primeiro aluno: ')
    nome2 = input('Digite o nome do segundo aluno: ')
    nome3 = input('Digite o nome do terceiro aluno: ')
    lista = [nome1, nome2, nome3]
    print('o aluno escolhiddo foi {}'.format(random.choice(lista)))
