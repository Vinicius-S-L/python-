

funcionario = float(input('Quanto você ganha: '))



if funcionario > 1250:
    funcionario = funcionario * 1.1
    print('Seu novo {1}salário{2} é {1}{0}{2}'.format(funcionario, '\033[1;31;40m', '\033[m'))
else:
    funcionario = funcionario * 1.15
    print('Seu novo {1}salário{2} é {1}{0}{2}'.format(funcionario, '\033[1;31;40m', '\033[m'))