"""
lamp1 = Lampada('branca', 110, 60)
lamp1.ligar_desligar() #alterna o estado da lampada.
print(f'A lampada está acesa? {lamp1.checa_lampada()}')

Ex.2 Forma Errada de acessar:
lamp1 = Lampada()
            ^^^^^^^^^
TypeError: Lampada.__init__() missing 3 required positional arguments: 'cor', 'voltagem', and 'luminosidade'

Ex.3

cli1 = Cliente('Angelina Jolie', '123.456.789.99')
cc1 = ContaCorrente(5000, 20000, cli1)
cc1.mostra_cliente()
cc1._ContaCorrente__cliente.diz() #Este acesso é fora do padrão mas funciona

"""


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente {self.__nome} diz oi')


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')


