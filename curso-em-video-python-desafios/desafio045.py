import time
import random


## usando as cores para prática, eu sei que não esta muito bonito, mas vou deixa assim porque quero foca em deixa mais prático o código
# aqui só a parte front do programa

print('{}{}{}'.format('\033[1;34;40m', '-='*20, '\033[m'))
print('Vamos jogar Jokenpô')
print('{}{}{}'.format('\033[1;34;40m', '-='*20, '\033[m'))
time.sleep(3)
print('Vou escolhe uma opção: pedra, papel, tesoura')
time.sleep(0.7)
print('Escolhi o meu')
print('Agora sua vez!!')

print('{}Processando.{}'.format('\033[7;37;40m', '\033[m'))

time.sleep(0.8)
print('{}Processando..{}'.format('\033[7;31;47m', '\033[m'))

time.sleep(0.8)
print('{}processando...{}'.format('\033[7;30;41m', '\033[m'))

time.sleep(0.8)
print('{}pronto!!{}'.format('\033[7;32;40m', '\033[m'))

print('\n{}{}{}'.format('\033[1;34;40m', '--'*20, '\033[m'))



# AGORA É O BACK DO PROGRAMA

opcoes = [None,'pedra', 'papel', 'tesoura']
bot = random.randint(1, 3)
pessoa = input("""Qual você escolhe? 
{0}[1]-pedra{1}
{0}[2]-papel{1}
{0}[3]-tesoura{1} \n  """.format('\033[7;30;41m', '\033[m'))
print('\n')

if bot == 1:
    if pessoa == 'pedra' or pessoa == '1':
        print("Opa! Deu Empate!")
    elif pessoa == 'papel' or pessoa == '2':
        print("Parabéns! VocÊ ganou!")
    elif pessoa == 'tesoura' or pessoa == '3':
        print('Infelizmente para você, eu ganhei ')
    else:
        print("Opção invalida!")

if bot == 2:
    if pessoa == 'pedra' or pessoa == '1':
        print('Infelizmente para você, eu ganhei ')
    elif pessoa == 'papel' or pessoa == '2':
        print("Opa! Deu Empate!")
    elif pessoa == 'tesoura' or pessoa == '3':
        print("Parabéns! VocÊ ganou!")
    else:
        print("Opção invalida!")

if bot == 3:
    if pessoa == 'pedra' or pessoa == '1':
        print("Parabéns! VocÊ ganou!")
    elif pessoa == 'papel' or pessoa == '2':
        print('Infelizmente para você, eu ganhei ')
    elif pessoa == 'tesoura' or pessoa == '3':
        print("Opa! Deu Empate!")
    else:
        print("Opção invalida!")

print('\n')

print('{}{}{}'.format('\033[1;34;40m', '___'*20, '\033[m'))
if pessoa.isnumeric() and pessoa in ['1', '2', '3']:
    pessoa = int(pessoa)
    print('''\nResultado da partida:
    Computador escolheu {0}{2}{1}
    Jogador escolheu {0}{3}{1}\n'''.format('\033[1;34;40m', '\033[m', opcoes[bot], opcoes[pessoa]))

if isinstance(pessoa, str):
    print('''\nResultado da partida:
    Computador escolheu {0}{2}{1}
    Jogador escolheu {0}{3}{1}\n'''.format('\033[1;34;40m', '\033[m', opcoes[bot], pessoa))

print('{}{}{}'.format('\033[1;34;40m', '___'*20, '\033[m'))

print('{}{}{}\n'.format('\033[1;34;40m','-='*20, '\033[m'))

print('{} vamos de novo!{}  '.format('\033[7;34;40m','\033[m'))