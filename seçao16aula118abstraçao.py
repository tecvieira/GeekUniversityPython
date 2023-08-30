class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'saldo de {self.__saldo} do titular {self.__titular} com limite {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente.')
        else:
            print('O valor deve ser positivo.')


# Testando
conta1 = Conta('Angelina Jolie', 150, 1500)
print(conta1.__dict__)
conta1.depositar(100)
print(conta1.__dict__)
conta1.sacar(45)
print(conta1.__dict__)

"""
Respostas:
/usr/bin/python3.11 /home/robsonvander/Documentos/GitHub/GeekUniversityPython/seçao16aula118abstraçao.py 
{'_Conta__numero': 400, '_Conta__titular': 'Angelina Jolie', '_Conta__saldo': 150, '_Conta__limite': 1500}
{'_Conta__numero': 400, '_Conta__titular': 'Angelina Jolie', '_Conta__saldo': 250, '_Conta__limite': 1500}
{'_Conta__numero': 400, '_Conta__titular': 'Angelina Jolie', '_Conta__saldo': 205, '_Conta__limite': 1500}
"""