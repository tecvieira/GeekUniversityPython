"""
Trabalhando com Json/ Pickle

ret = jsonpickle.encode(felix) => esta função vai modelar nosso objeto para o formato jasonpickle.

saída => {"py/object": "__main__.Gato", "_Gato__nome": "Felix", "_Gato__raca": "vira Lata"}
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
ret = jsonpickle.encode(felix)
print(ret)
