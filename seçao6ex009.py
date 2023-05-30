from time import sleep
n = 1
print('\033[34m*** Veja os "N" números naturais e ímpares da sequência ***\033[m')
num = int(input('Informe um número: '))
if num < 0:
    print(f'\033[31mERRO! este número {num} não é natural, escolha um número positivo.\033[m')
else:
    while n <= num:
        if n % 2 == 1 and num >= 0:
            print(f' {n} ->', end='')
            sleep(0.2)
        n += 1
print(' Fim...')
