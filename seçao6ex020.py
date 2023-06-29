somapar = 0
somatodos = 0
num = 0
while True:
    num = int(input('Informe um número inteiro e verifique se é par: '))
    somatodos += 1
    if num % 2 == 0:
        print(f'O número {num} é par!')
        somapar = somapar + 1
    else:
        print(f'Este número {num} é impar')
    resp = int(input(' Deseja continuar? 0 para ficar ou 1000 para sair'))
    if resp == 1000:
        break
print(f'Foram informados {somatodos} números.')
print(f'Destes números apenas {somapar} é par.')
print('Fim...')
