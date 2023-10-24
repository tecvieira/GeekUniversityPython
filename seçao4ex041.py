"""from time import sleep
vl_hora = float(input('Informe o valor da hora trabalhada: R$ '))
qtd_hora = float(input('Quantidade de horas trabalhadas: '))
print('Calculando o valor a receber...')
sleep(1)
valor = (qtd_hora * vl_hora)
print(f'Horas trabalhadas.... {qtd_hora}'
      f'Valor da hora .......{vl_hora:.2f}'
      f'Total a receber R${valor:.2f}')
"""


def valor_hora(hora, valor):
    """Calcula o valor da hora trabalhada"""
    calculo = hora * valor
    aumento = (calculo * 10) / 100
    return print(f'O valor da hora trabalhada com 10% de acrescimo R$ {calculo + aumento:.2f}')


hor = float(input('Quantas horas trabalhadas: '))
val = float(input('Qual o valor da hora: '))
valor_hora(hor, val)
