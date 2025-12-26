#Tarefa: Rafaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher
# só que agora utilizando um laço for.

valor = int(input('Digite o número para ver sua tabuada: '))
print('{}{}{}'.format('\033[1;28;40m','__'*10, '\033[m'))

for c in range(1,11):
    print('{} x {} = {}'.format(valor,c,valor*c))

print('{}{}{}'.format('\033[1;28;40m','__'*10, '\033[m'))