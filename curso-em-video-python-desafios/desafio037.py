numero = int(input('Digite um número qualquer: '))
escolha = input('Qual das opções quer que converta esse número \n 1-Binário\n 2-octal\n 3-hexadecimal\n ').title()

if escolha == 'Binário' or '1' in escolha:
    numero = bin(numero)
    print(numero[2:])
elif escolha == 'octal' or '2' in escolha:
    numero = oct(numero)
    print(numero[2:])
elif escolha == 'hexadecimal' or '3' in escolha:
    numero = hex(numero)
    print(numero[2:])
else:
    print('Desculpa, mas não tem esssa opção')