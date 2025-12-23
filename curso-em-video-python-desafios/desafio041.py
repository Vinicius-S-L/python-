import datetime

nasc = int(input('Digite o ano de nascimento: '))
hoje = datetime.date.today()
anos = hoje.year - nasc

if anos <= 9:
    print('Você é um atleta Mirim')
elif anos <= 14:
    print('Você é um atleta Infantil')
elif anos <= 19:
    print('Você é um atleta Junior')
elif anos <= 20:
    print('Você é um atleta Sênior')
else:
    print('Você é um atleta Master')