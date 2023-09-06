"""
Em linguagens de programaçao como Java, ao declararmos atributos privados nas classes, costumamos a criar métodos
públicos para manipulaçãodesses atributos. Esses métodos são conhecidos por getters e setters, onde os getters retornam
o valor do atributo e o setters alteram o valor do mesmo.

Respostas dos testes propostos:
=> Saldo de: 3000 do cliente: Felicity
=> Saldo de: 2000 do cliente: Angelina
=> A soma do saldo das conta1 e conta2 é: 5000
=> {'_Conta__numero': 1, '_Conta__titular': 'Felicity', '_Conta__saldo': 3000, '_Conta__limite': 5000}
+> {'_Conta__numero': 2, '_Conta__titular': 'Angelina', '_Conta__saldo': 2000, '_Conta__limite': 4000}
"""


class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'Saldo de: {self.__saldo} do cliente: {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    def get__numero(self):
        return self.__numero

    def get__titular(self):
        return self.__titular

    def set__titular(self, titular):
        self.__titular = titular

    def get__saldo(self):
        return self.__saldo

    def get__limite(self):
        return self.__limite

    def set__limite(self, limite):
        self.__limite = limite


conta1 = Conta('Felicity', 3000, 5000)
conta2 = Conta('Angelina', 2000, 4000)


print(conta1.extrato())
print(conta2.extrato())
soma = conta1.get__saldo() + conta2.get__saldo()
print(f'A soma do saldo das conta1 e conta2 é: {soma}')
print(conta1.__dict__)
print(conta2.__dict__)
