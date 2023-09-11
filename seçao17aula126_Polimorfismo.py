"""
Polo => Muitas
Morfis => Formas

- Quando reimplantamos um método presente na classe pai em classes filhas estamos realizando uma sobrescrita de
métodos (overriding).
- O overriding é a melhor representação do polimorfismo.
- No exemplo abaixo a classe animal se comporta de diversas formas de acordo com o animal herdado, representando
o polimorfismo, principalmente no método falar onde cada animal possui uma caracteristica diferente.
- Não implementar o método falar vai gerar uma excessão do tipo: NotImplementedError prevista na classe animal.

Saida dos testes:
Felix está comendo...
Felix fala miau
Pluto está comendo...
Pluto fala wau wau
Mickey está comendo...
Mickey fala algo!
"""


class Animal(object):
    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método')

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Cachorro(Animal):
    def __init__(self, nome):
        super(). __init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala wau wau')


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau')


class Rato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala algo!')


felix = Gato('Felix')
felix.comer()
felix.falar()

pluto = Cachorro('Pluto')
pluto.comer()
pluto.falar()

mickey = Rato('Mickey')
mickey.comer()
mickey.falar()
