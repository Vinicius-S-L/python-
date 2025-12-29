#Tarefa: Malhora o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 a 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpitas foram necessários para vencer.

from random import randint
from emoji import emojize

bot = randint(0, 10)
tentativa = 0
while True:

    jogador = int(input('Digite um numero de 0 a 10: '))
    tentativa += 1

    if bot == jogador:
        print(f'Parabéns você acertou! era {bot}\n')
        break
    elif bot > jogador:
        print('Pensei em maior. ')
    else:
        print('Pensei em um número menor\n')

print(emojize(f'Fim de jogo :thumbsup:, você precisou de {tentativa} tentativas', language='alias'))