# Tarefa: Cria um programa que leia dois valores a mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Sau programa deverá realizar a operação solicitada em cada caso.

numero1 = input('Digite um numero aleatório: ').strip().lower()
numero2 = input('Digite outro numero: ').strip().lower()

while True:

    print('-'*30)
    escolha = input(''' Escolha uma opção \n
     [1] somar
     [2] multiplicar
     [3] maior
     [4] novos números
     [5] sair do programa\n''').strip().lower()
    if escolha in ['1', 'somar']:
        soma = numero1 + numero2
        print(f' {numero1} + {numero2} = {soma}')
    elif escolha in ['2', 'multiplicar']:
        multiplicar = numero1 * numero2
        print(f' {numero1} * {numero2} = {multiplicar}')
    elif escolha in ['3', 'maior']:
        if numero1 > numero2:
            print(f'O {numero1} é maior que {numero2}')
        elif numero1 < numero2:
            print(f'O {numero2} é maior que {numero1}')
        else:
            print(f'Os dois números são iguais')
    elif escolha in ['4', 'novos', 'números']:
        print('Ok')
        numero1 = int(input('Digite um numero aleatório: '))
        numero2 = int(input('Digite outro numero: '))

    elif escolha in ['5', 'sair']:
        break
    else:
        print('Opço invalida! tente novamente')

print('Programa encerrado. Até logo!')