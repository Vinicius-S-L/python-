salario = float(input('Digite o salário de seu funcionário: '))
aumento = salario * 0.15
print('Se seu funcionário tiver um aumento de 15%, vai ter {:.2f} reais a mais, sendo assim {:.2f} reais no novo salário'.format(aumento, salario + aumento))