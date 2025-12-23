

emprestimo = float(input('Qual o valor do emprestimo: '))
salario = float(input('Qual o valor do seu salorio: '))
tempo = float(input('Quantos anos deseja pagar: '))

mensalidade = emprestimo / (tempo * 12)

if mensalidade > salario * 0.3:
    print('Emprestimo negado! o valor da mensalidade bateu {1}30%{2} a mais do seu salário: {0}'.format(mensalidade, '\033[7;31;40m','\033[m'))
else:
    print('Emprestimo aprovado!  o valor da mensalidade é {}'.format(mensalidade) )