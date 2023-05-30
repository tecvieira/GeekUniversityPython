from time import sleep
notas = 1000
while notas <= 100000:
    print(f'{notas} * ', end='')
    notas += 1000
    sleep(0.2)
print('FIM')
