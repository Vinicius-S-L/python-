from time import sleep
from random import randint
# contador, tarefa era fazer um contador para fogos de artifícios

fim_cor = '\033[m'
for c in range(10,-1, -1):
    cor = '\033[1;{};40m'.format(randint(91, 97))
    print('{0}{2}{1}'.format(cor,fim_cor, c))
    sleep(1)
print('\033[1;34;40m{}\033[m'.format('BOOM!! CABUM!! BOOOMM'))