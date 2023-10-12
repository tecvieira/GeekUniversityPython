"""
#Escrevendo arquivo jsonpickle

import jsonpickle


class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'vira Lata')
with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)

# LENDO UM ARQUIVO JSON
import jsonpickle


class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'vira Lata')
with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)

print(ret)
print(type(ret))
print(ret.nome)
print(ret.raca)

SAÍDA DE RESPOSTA
<__main__.Gato object at 0x7f15bf25e320>
<class '__main__.Gato'>
Felix
vira Lata

"""
import jsonpickle


class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'vira Lata')
with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)

print(ret)
print(type(ret))
print(ret.nome)
print(ret.raca)
