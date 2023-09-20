"""
Saída =>
<bound method Gato.__init__ of <__main__.Gato object at 0x7fb04e8d2bf0>>
{"_Gato__nome": "Felix", "_Gato__raca": "Vira-lata"}
"""

import json

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

felix = Gato('Felix', 'Vira-lata' )
print(felix.__init__)
ret = json.dumps(felix.__dict__)
print(ret)
