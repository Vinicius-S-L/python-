#tTarefa: Desenvolva um programa que leia o primeiro termo a a razão de uma PA. No final
# mostre os 10 primeiros termos dessa progressão.

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))

# use a variável 'c' do for para mostra os termos de forma mais visível

for c in range(1, 11):
    print( end='[{0}-{1}]    '.format(c, termo))
    termo += razao
print('\nFim da progressão.')