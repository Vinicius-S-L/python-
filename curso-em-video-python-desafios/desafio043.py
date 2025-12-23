
peso = float(input('Digite o seu peso(km): '))
altura = float(input('Digite sua altura(m): '))

imc = peso / (altura * altura)
print('O IMC é {:.1f} '.format(imc))

if imc < 18.5:
    print('Abaixo do imc')
elif imc < 25:
    print('Peso ta ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')