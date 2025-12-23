

valor = float(input('Digite um valor da compra: '))


pagamento = input('Qual a sua forma de pagamento: \n [1]- dinheiro/cheque\n [2]- á vista/cartão\n [3]- 2x no cartão\n [4]- 3x ou mais no cartão\n ')

if pagamento == '1' or pagamento == 'dinheiro':
    valor_dinheiro = valor * 90/100
    print('Você vai pagar R$ {:.2f}, já tendo o desconto de 10%'.format(valor_dinheiro))
elif pagamento == '2' or 'á vista' in pagamento:
    valor_vista = valor * 95/100
    print('Você vai pagar R$ {:.2f}; já tendo o desconto de 5%'.format(valor_vista))

elif pagamento == '3' or pagamento == '2x':
    print('Você vai pagar R$ {:.2f}, sem desconto'.format(valor))
elif pagamento == '4' or pagamento == '3x':
    print('Você vai pagar R$ {:.2f}; já tendo juros de 20%'.format(valor * 1.2))
else:
    print("ERROr, opção invalida!")