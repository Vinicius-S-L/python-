metros = float(input('Digite um número: '))
print('Esse valor de {0} metros'.format(metros))
print(' em {0}km \n em {1}hm \n em {2}dam'.format(metros / 1000, metros / 100, metros / 10))
print(' em {3}dm \n em {1}cm \n em {2:.0f}mm'.format(metros, metros * 100, metros * 1000, metros * 10 ))