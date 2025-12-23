frase = input('Digite uma frase: ').strip().lower()

print('tem {} letra "a" na frase:'.format(frase.count('a')))
print('a primeira letra "a" está na posição (os espaços contam): {}'.format(frase.find('a')+1))

print('A ultima letra a "a" esta na posição (os espaços contam): {}'.format(frase.rfind('a')+1))