#Tarefa: Cria um programa que leia o ano de nascimento de sete pessoas.
# No final. mostra quantas pessoas ainda não atingiram a maioridade a quantas já SÃO maiores.

import datetime
hoje = datetime.date.today().year
pessoas_maiores_de_idade = 0
pessoas_menores_de_idade = 0


for c in range(1, 7+1):
    data = int(input('Qual a sua data de nascimento: '))
    maior_idade = hoje - data

    if maior_idade >= 18:
        print('Já é maior de idade com {0} anos, próximo!!\n'.format(maior_idade))
        pessoas_maiores_de_idade += 1
    else:
        print('Ainda não é de maior idade, tem apenas {} anos\n'.format(maior_idade))
        pessoas_menores_de_idade +=1
print('{1}Há {0} pessoa(s) de maiores de idade!{2}\n'.format(pessoas_maiores_de_idade, '\033[7;37;40m', '\033[m'))
print('{1}E há apenas {0} pessoa(s) sendo menor(es) de idade!{2}\n'.format(pessoas_menores_de_idade, '\033[7;37;40m', '\033[m'))
