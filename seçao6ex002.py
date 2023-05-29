print('\033[32m=== Contagem de 1 a 100 utilizando o "for"=== \033[m')
for numeros in range(1, 101, 1):
    print(f'{numeros}', end='')
    if numeros < 100:
        print('->', end=' ')
print('\n\033[32mFim da lista com for\033[m')
print('\033[34m*** Listagem de 1 a 100 usando o while ***\033[m')
numeros = 0
while numeros < 101:
    print(f'{numeros}', end=' ')
    numeros += 1
print('\n\033[34mFim da lista com while\033[m')




