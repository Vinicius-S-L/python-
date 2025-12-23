numero = int(input('Digite um número: '))
print('{0}{1}{2}'.format('\033[1;31;40m', '-='*20, '\033[m'))
if numero % 2 == 0:
    print('Esse número {} é par'.format(numero))
else:
    print('Esse número {} é impar'.format(numero))
print('{0}-={1}'.format('\033[1;31;40m','\033[m' )*20)