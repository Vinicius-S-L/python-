numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))
numero3 = int(input('Digite o terceiro numero: '))

if numero1 > numero2 and numero1 > numero3:
    print('O número {} é o maior'.format(numero1))
if numero2 > numero1 and numero2 > numero3:
    print('O número {} é o maior'.format(numero2))
else:
    print('O número {} é o maior'.format(numero3))


if numero3 < numero1 and numero3 < numero2:
    print('O número {} é o menor'.format(numero3))
if numero1 < numero3 and numero1 < numero2:
    print('O número {} é o menor'.format(numero1))
else:
    print('O número {} é o menor'.format(numero2))