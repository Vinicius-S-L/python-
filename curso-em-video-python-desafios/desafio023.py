numero = int(input('Digite um numero entre 0 e 9999: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10


print('milhar é {}'.format(milhar))
print('centena é {}'.format(centena))
print('dezena é {}'.format(dezena))
print('unidade é {}'.format(unidade))
