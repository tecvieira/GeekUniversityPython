"""
# importando um pacote em Geek
from Geek import geek1
print(geek1.funcao(4, 6))
=> 10

# importando dois pacotes em Geek
from Geek import geek1, geek2

print(geek1.funcao(10, 9))
print(geek2.funcao2())
=> 19
=> Programação em Python Essencial

# Fazendo acesso a função de um sub pacote.
from Geek.university import geek3, geek4

print(geek3.funcao3())
=> Geek
print(geek4.funcao4())
=> Univerity

# Fazendo acesso apenas uma função do sub pacote
from Geek.university.geek4 import funcao4
print(funcao4())
=> University
"""
from Geek.university.geek4 import funcao4
print(funcao4())

