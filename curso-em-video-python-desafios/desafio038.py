numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo: '))

if numero1 > numero2:
    print('O número {} é maior que {}'.format(numero1, numero2))
elif numero1 < numero2:
    print('O número {} é maior que {}'.format(numero2, numero1))
else:
    print('O Dois número são iguais')