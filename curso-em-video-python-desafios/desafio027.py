nome = input('Digite seu nome completo: ')

primeiro_nome = nome.split()[0]     ## faz uma lista que pegar o primeiro item da lista
total = len (nome.split())          ## conta quantos itens tem na lista
ultimo_nome = nome.split()[total-1] ## diminui o valor de len, pós len não conta usando o 0(zero) como o primeiro número então tem que mininuir -1 para não ter erro de leitura

print('nome completo: {}'.format(nome.title()))
print('primeiro nome: {}'.format(primeiro_nome))
print('ultimo nome: {}'.format(ultimo_nome))
