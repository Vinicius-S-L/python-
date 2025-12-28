#Tarefa: Desenvolva um programa que leia o nome, idade a sexo de 4 pessoas. No final do programa, mostre:
#   A média de idade do grupo.
#   Qual é o nome do homem mais velho.
#   Quantas mulheres tëm menos de 20 anos.

nome_do_mais_velho = ''
soma_idade = 0
homem_mais_velhor = 0
mulheres_menor_de_20 = 0
for c in range(1,5):
    print('-'*30)
    nome = str(input('Digite o nome da {}° pessoa: '.format(c))).title().strip()
    idade = int(input('Digite a idade da {}° pessoa: '.format(c)))
    sexo = str(input('Digite o sexo da {}° pessoa: [M/F] '.format(c))).upper()
    print('-'*30)
    soma_idade += idade

    if homem_mais_velhor == 0 and sexo == 'M':
        homem_mais_velhor = idade
        nome_do_mais_velho = nome
    elif idade > homem_mais_velhor and sexo == 'M':
        homem_mais_velhor = idade
        nome_do_mais_velho = nome

    if sexo == 'F' and 20 > idade:
        mulheres_menor_de_20 +=  1


media = soma_idade / 4
print('\nA média do grupo foi: {}'.format(media))
print('\nO nome do homem mais velho é {} e tem  {} anos'.format(nome_do_mais_velho, homem_mais_velhor))
print('\nNúmeros de mulheres que têm menos de 20 anos: {}'.format(mulheres_menor_de_20))