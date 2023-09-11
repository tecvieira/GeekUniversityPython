"""
Herança multipla nada mais é do que a possibilidade de uma classe herdar de multiplas classes, fazendo com que
a classe filha receba/ herde todosos atributos e métodos de todas as classes herdadas.

Obs. A herança muktipls pode ser feita duas maneiras:
Por multiderivação direta, ou por multiderivação Indereta.

Obs. Não importa se a derivação é direta ou indireta, a classe que herdar a herança recebe todos os atributos e métodos
da super classe.
Saída dos Testes:
Wally está nadando.
Eu sou Wally do mar
Xim está andando.
Eu sou Xim da terra!
Tux está andando.
Tux está nadando.
Eu sou Tux da terra! # A ordem de herança faz diferença na execução dos métodos, neste caso a saída foi da
                       da terra pois Terrestre estava em primeiro lugar na hordem de herança.
"""


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimento(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando. '

    def cumprimento(self):
        return f'Eu sou {self._Animal__nome} do mar'


class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando.'

    def cumprimento(self):
        return f'Eu sou {self._Animal__nome} da terra!'


class Pinguim(Terrestre, Aquatico):
    def __init__(self, nome):
        super().__init__(nome)


baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimento())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimento())

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimento())
