from datetime import datetime
from time import sleep

print('=== CALCULANDO VALOR DO PRÊMIO ===')
data_hora = datetime.now()
data_hora_txt = data_hora.strftime('%d/%m/%y - %H:%M\n')
print(data_hora_txt)
valor_total = float(input('Informe o valor total do prêmio R$ '))
print('Calculando...')
sleep(3)
print(f'\033[34mO primeiro ganhador vai receber R$ {valor_total * (46/100):.2f}\033[m')
sleep(2)
print(f'\033[32mO segundo ganhador vai receber R$ {valor_total * (32/100):.2f}\033[m')
sleep(1)
print(f'\033[33mO terceiro colocado receberá R$ {valor_total * (22/100):.2f}\033[m')
print('\033[31mAcredite na sorte!!!\033[m')

