

cateto_oposto = float(input('Digite o \033[1;30;47mcateto oposto:\033[m '))
cateto_adjacente = float(input('Digite o \033[1;32;40mcateto adjacente:\033[m '))
hipotenusa = float(input('Digite o valor da \033[1;31;42mhipotenusa:\033[m '))

if cateto_oposto + hipotenusa < cateto_adjacente or cateto_oposto > hipotenusa + cateto_adjacente   :
    print('Esse valores não podem forma um \033[2;34;40mtriangulo\033[m')
else:
    print('Esse valores podem forma um \033[2;34;40mtriangulo\033[m')