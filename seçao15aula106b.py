"""
Funçoes Aninhadas - Nested Functions
Em Python podemos ter funções dentro de funções, que são conhecidas por Nested Functions ou também Inner Functions
(Funções Internass)
Exemplos

Obs. Ao executar a função humor(), choice escolhe de forma aleatória dentre as opções.
"""
from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de voçê '))
    return humor() + pessoa


#Testando

print(cumprimento('Angelina'))
print(cumprimento('Felicity'))
