"""
Delta é a diferença entre a hora e data final menos hora e data inicial

data_inicial = datetime.datetime(1969,7,5 )
data_final = datetime.datetime.now()
quantidade_anos = data_final - data_inicial
print(quantidade_anos)
=> 19811 days, 16:31:56.116857
print(f'Ele possui {(quantidade_anos.days)/ 365:.0f} anos de idade.')
=> Ele possui 54 anos de idade.

Configurando Boleto:
Adicionando 3 dias a data atual como vencimento do boleto

data_compra = datetime.datetime.now()
regra_boleto = datetime.timedelta(days=3)
vencimento_boleto = data_compra + regra_boleto
print(vencimento_boleto)
=> 2023-10-04 16:40:22.766535
"""

import datetime

data_compra = datetime.datetime.now()
regra_boleto = datetime.timedelta(days=3)
vencimento_boleto = data_compra + regra_boleto
print(vencimento_boleto)

