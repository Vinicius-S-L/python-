#Tarefa: Faça um programa que leia o peso de cinco pessoas.
# No final, mostra qual foi o maior a o menor peso lidos.
peso_maior = 0
peso_menor = 0
for c in range(1,6):
    peso = float(input('Digite o peso da {}° pessoa: '.format(c)))
    if c == 1:
        peso_maior = peso
        peso_menor = peso

    if peso >= peso_maior:
        peso_maior = peso
    elif peso <= peso_menor:
        peso_menor = peso


print('O menor peso foi {} e o maior peso foi {}'.format(peso_menor, peso_maior))