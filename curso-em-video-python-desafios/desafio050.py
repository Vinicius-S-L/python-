#Tarefas: Desenvolva um programa que leia seis números inteiros a mostra a soma apenas daqueles que forem pares.
# Se o valor digitado for impar. desconsidere-o.

numeros_pares = []
for c in range(1,7):
    numero = int(input("Digite um número (preciso de 6 números):   "))
    if numero % 2 == 0:
        numeros_pares.append(numero)
total = sum(numeros_pares)
print('A soma de todos os numero pares são: {}'.format(total))