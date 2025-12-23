dia = int(input('Por quantos dias eu aluguei o carro:  '))
distancia = int(input('Por quantos km eu andei de carro: '))

valor_dia = dia * 60
valor_km = distancia * 0.15

print('Você irá pagar um total de R${:.2f}'.format(valor_dia + valor_km))
