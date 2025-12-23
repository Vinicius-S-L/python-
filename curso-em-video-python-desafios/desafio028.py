from random import randint
import emoji
numero = randint(1, 5)

tentativa = int(input('Escolha um numero de 1 a 5: '))
fim =  emoji.emojize('Fim de jogo, até a proxima :thumbsup:', language='alias')

if tentativa == numero:
    print('Parabéns você acertou! era {}'.format(tentativa))
elif tentativa > numero:
    print('Eu pensei no número {}'.format(numero))
    print(fim)
else:
    print('eu pensei no numero {}'.format(numero))
    print(fim)