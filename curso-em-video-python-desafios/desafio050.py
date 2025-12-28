#Tarefas: Desenvolva um programa que leia seis números inteiros a mostra a soma apenas daqueles que forem pares.
# Se o valor digitado for impar. desconsidere-o.

numeros_pares = 0
total = 0

for c in range(1,7):
    numero = int(input("Digite o {}° número:   ".format(c)))
    if numero % 2 == 0:
        total += numero
        numeros_pares += 1
print('A soma de todos os numero pares são: {}'.format(total))
print('Lista dos números pares: {}'.format(numeros_pares))