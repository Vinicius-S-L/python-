frase = input('Digite uma frase para ver se é um políndromo: ').lower()
# deixo a frase inversa, mas mantem os espaços
frase_inverso = frase[::-1]

# agora pego as frases, tiro os espaço entres as palavras e comparo com ambos

if frase.replace(' ', '') == frase_inverso.replace(' ', ''):
    print('{} é um Palíndromo'.format(frase))
else:
    print('{} não é um Palíndromo'.format(frase))