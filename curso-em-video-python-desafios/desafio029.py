velocidade = int(input('Qual a velocidade do carro? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('você foi multado no valor {1}R${0:.2f}{2} por ultrapassado o limite de 80km'.format(multa, '\033[1;32;40m', '\033[m'))
