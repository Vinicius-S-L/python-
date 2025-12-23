largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual é a altura da parede? '))
area = largura * altura
tinta = area / 2
print('Você tem uma parede de {0}x{1} {2} m² e vai precisa {3} litro de tinta.'.format(largura, altura, area, tinta))