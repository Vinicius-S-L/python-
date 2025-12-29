# Tarefa: Melhora o DESAFIO 061. Perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar O termos.

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
progressao = 1
total = 10
mais = 0

while True:
    while progressao <= total:

            print(f'{termo}', end='-')
            termo += razao
            progressao += 1
    mais = int(input('\nQuer quantos mais termo? '))
    if mais == 0:
        break
    total += mais

print(f'\nProgressão finalizada com {progressao - 1} termos exibidos.')
