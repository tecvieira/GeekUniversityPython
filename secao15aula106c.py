"""
Inner Functions
Funções Internas podem acessar o escopo de funções mais externas.

A variavél rindo vai receber uma função (faz_me_rir_novamente(pessoa) ) com um argumento (Fernanda)
ao executar a variavel executamos a função e o choice de forma aleatŕia escolhe que tipo de rizada.
"""
from random import choice


def faz_me_rir_novamente(pessoa):
    def dando_rizada():
        risada = choice(('hahaha', 'kakaka', 'kikiki'))
        return f'{risada} {pessoa}'
    return dando_rizada


rindo = faz_me_rir_novamente('Fernanda')
print(rindo())
print(rindo())
print(rindo())
