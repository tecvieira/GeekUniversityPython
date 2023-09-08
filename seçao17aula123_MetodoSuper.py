"""
O método super se refere a super classe.
Com o método super() podemos fazer acesso a qualquer elemento da classe pai,
ou seja, atributos e métodos e não somente ao constrututor.
Ex. super().faz_som('auauaua')

Saida do teste:
=> O Felix faz miau
"""


class Animal:
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O {self.__nome} faz {som}')


class Gato(Animal):
    def __init__(self, nome, especie, raca):
        Animal.__init__(self, nome, especie) #é possível fazer assim mas não é correto
        super().__init__(nome, especie) # esta é forma correta
        self.__raca = raca


felix = Gato('Felix', 'felino', 'angora')
felix.faz_som('miau')
