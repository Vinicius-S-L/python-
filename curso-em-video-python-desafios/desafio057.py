#Tarefa: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#Caso estaja errado, peça a digitação novamente até ter um valor correto

    
while True:
    sexo = str(input('Digite seu sexo: [M/F] : ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('Sexo invalido. Tente novamente.')
    else:
        break
print('ok, próximo')

