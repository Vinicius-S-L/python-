import time
# contador, tarefa era fazer um contador para fogos de artifícios
for c in range(10,0, -1):
    print('{0}{2}{1}'.format('\033[1;34;40m','\033[m', c))
    time.sleep(1)
    if c == 1:
        print('\033[1;34;40m{}\033[m'.format('BOOM!!'))