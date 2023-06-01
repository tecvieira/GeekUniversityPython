from time import sleep
print('==== CONVERTENDO DE Km/H PARA m/s ====')
velK = float(input('             INFORME A VELOCIDADE EM km/h :'))
print('\033[35m-=\033[m' * 30)
print('Convertendo....')
sleep(1.0)
velM = velK / 3.6
print('\033[35m-=\033[m' * 30)
print(f'\033[35mVelocidade {velK:.2f} Km/h   => \033[m \033[32mVelocidade {velM:.2f} m/s\033[m' )
print('\033[35m-=\033[m' * 30)
print('ByTecVander v.1.0')
