#Tarefa: Faça um programa que leia um número inteiro a diga sa ala é OU NÃO Um número primo.

#A forma mais segura de verificar se um número é primo é contar quantas vezes ele foi dividido exatamente (resto zero)
# entre 1 e ele mesmo. Se o total de divisões for 2, ele é primo.

total_divisoes = 0

numero = int(input('Digite um número para verificar se é um número primo:   '))
for c in range(1, numero+1):
    if numero % c == 0:
        total_divisoes += 1

if total_divisoes == 2:
    print('número primo')
else:
    print('Não é número primo')