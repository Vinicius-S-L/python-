viagem = float(input('Qunatos km de viagem: '))

if viagem <= 200:
    viagem = viagem * 0.50
    print('Sua viagem vai custar R${:.2f}'.format(viagem))
else:
    viagem = viagem * 0.45
    print('Sua viagem vai custar R${:.2f}'.format(viagem))