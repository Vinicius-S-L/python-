nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 7:
    print('Aprovado: {}'.format(media))
elif media >= 5 and media <= 6.9:
    print('recuperação: {}'.format(media))
else:
    print('reprovado: {}'.format(media))