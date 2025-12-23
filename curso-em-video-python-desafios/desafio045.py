import time
import random

bot = random.choice(['pedra', 'papel', 'tesoura'])
## usando as cores para prática, eu sei que não esta muito bonito, mas vou deixa assim

print('{}{}{}'.format('\033[1;34;40m', '-='*20, '\033[m'))
print('Vamos jogar Jokenpô')
print('{}{}{}'.format('\033[1;34;40m', '-='*20, '\033[m'))
time.sleep(3)
print('Vou escolhe uma opção: pedra, papel, tesoura')
time.sleep(0.7)
print('Escolhi o meu')
print('Agora sua vez!!')
pessoa = input("Qual você escolhe? {}(pedra, papel, tesoura){}:  ".format('\033[7;30;41m', '\033[m')).lower()


print('{}Processando.{}'.format('\033[7;37;40m', '\033[m'))

time.sleep(0.8)
print('{}Processando..{}'.format('\033[7;31;47m', '\033[m'))

time.sleep(0.8)
print('{}processando...{}'.format('\033[7;30;41m', '\033[m'))

time.sleep(0.8)
print('{}pronto!!{}'.format('\033[7;32;40m', '\033[m'))

print('\n{}{}{}'.format('\033[1;34;40m', '--'*20, '\033[m'))
# verificador de pedra

if pessoa == 'pedra' and bot == 'papel':
    print('Infelizmente, Você perdeu!')
    print('eu escolhi {} e você escolheu {}'.format(bot, pessoa))
elif pessoa == 'pedra' and bot == 'tesoura':
    print('Parabéns!! você ganhou!')
    print('eu escolhi {} e você escolheu {}'.format(bot, pessoa))
elif pessoa == 'pedra' and bot == 'pedra':
    print('Empate! vamos denovo!')
    print('eu escolhi {} e você escolheu {}'.format(bot, pessoa))

# verificador de tesoura

elif pessoa == 'tesoura' and bot == 'papel':
    print('Parabéns!! você ganhou!')
    print('eu escolhi {} e você escolheu {}'.format(bot, pessoa))
elif pessoa == 'tesoura' and bot == 'tesoura':
    print('Empate! vamos denovo!')
    print('eu escolhi {} e você escolheu {}'.format(bot, pessoa))
elif pessoa == 'tesoura' and bot == 'pedra':
    print('Infelizmente, Você perdeu!')
    print('eu escolhi {} e você escolheu {}'.format(bot, pessoa))

# verificador de papel

elif pessoa == 'papel' and bot == 'tesoura':
    print('Infelizmente, Você perdeu!')
    print('eu escolhi {} e você escolheu {}'.format(bot, pessoa))
elif pessoa == 'papel' and bot == 'pedra':
    print("Parabéns, você ganhou!")
    print('eu escolhi {} e você escolheu {}'.format(bot, pessoa))
elif pessoa == 'papel' and bot == 'papel':
    print('Empate! vamos denovo!')
    print('eu escolhi {} e você escolheu {}'.format(bot, pessoa))

print('{}{}{}\n'.format('\033[1;34;40m','-='*20, '\033[m'))

print('{} vamos de novo!{}  '.format('\033[7;34;40m','\033[m'))