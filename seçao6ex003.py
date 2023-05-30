from time import sleep
num = 10
while num > -1:
    print(f'{num} -> ', end='')
    num += -1
    sleep(0.5)
print('Fim...')
