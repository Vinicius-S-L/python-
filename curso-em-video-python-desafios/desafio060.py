# Tarefa: Faça um programa que leia um número qualquer a mostre o sau fatorial.
# Ex: 5 = 5x4x3x2x1 = 120

from math import factorial

numero = int(input('Digite um número:   '))

#Sem isso, o computador processa o mesmo número para sempre
# e precisa fazer a maquina mostra cada número antes do número escolhido
c = numero

print(f'{numero}! = ', end='')

while c != 0:
    print(f'{c}', end=' ')
    print('x'
          if c > 1
          else '=', end=' ')
    c -= 1

#usei o import de math para ter a opção factorial para fazer o calculo
print(factorial(numero))