# Tarefa: Rafaça o DESAFIO 051,
# lendo o primeiro termo a a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
progressao = 1

while True:
    if progressao <= 10:
        print(f'{termo}', end='->')
        termo += razao
        progressao += 1
    else:
        break

print('Fim!')