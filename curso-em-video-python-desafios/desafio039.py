import datetime
data_hoje = datetime.date.today()

nasc = int(input('Digite o ano de nascimento: '))
alista = data_hoje.year - nasc
print(alista)

if alista > 18:
    print('{}Você passou do tempo para se alistar:{}seu alistamento foi em {}'.format('\033[1;37;40m', '\033[m', ))
elif alista < 18:
    print('{}Ainda não chegou a idade para se alistar!{}'.format('\033[1;31;48m', '\033[m'))
else:
    print('{}Tem idade para se alistar!{}'.format('\033[1;30;42m', '\033[m'))

#(data_hoje.year) - Saída: 2025-12-18 (formato ano-mês-dia)
