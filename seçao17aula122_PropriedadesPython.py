"""
Aplicando propriedades python.

Respostas aos testes:
Saldo de: 3000 do cliente: Felicity
Saldo de: 2000 do cliente: Angelina
A soma do saldo das conta1 e conta2 é: 5000
{'_Conta__numero': 1, '_Conta__titular': 'Felicity', '_Conta__saldo': 3000, '_Conta__limite': 5000}
{'_Conta__numero': 1, '_Conta__titular': 'Felicity', '_Conta__saldo': 3000, '_Conta__limite': 76543}
76543
79543
6000
"""


class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    @property
    def valor_total(self):
        return self.__saldo + self.__limite

    def extrato(self):
        return f'Saldo de: {self.__saldo} do cliente: {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor


conta1 = Conta('Felicity', 3000, 5000)
conta2 = Conta('Angelina', 2000, 4000)


print(conta1.extrato())
print(conta2.extrato())
soma = conta1.saldo + conta2.saldo
print(f'A soma do saldo das conta1 e conta2 é: {soma}')
print(conta1.__dict__)
conta1.limite = 76543
print(conta1.__dict__)
print(conta1.limite)

print(conta1.valor_total)
print(conta2.valor_total)
