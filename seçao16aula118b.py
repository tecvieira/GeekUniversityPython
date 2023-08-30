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


    def transferir(self, valor, conta_destino):
        #1 - Remover o valor da conta origem
        self.__saldo -= valor
        # taxa de transferencia
        self.__saldo -= 10
        #2 - Adiciona o valor na conta destino
        conta_destino.__saldo += valor


print('Saldo Inicial')
conta1 = Conta('Angelina', 150.00, 1500)
conta1.extrato()

conta2 = Conta('Felicity', 300, 2000)
conta2.extrato()

print('Fazendo tranferência:')
conta2.transferir(100, conta1)
print('-=' * 15)
conta1.extrato()
conta2.extrato()
"""
/usr/bin/python3.11 /home/robsonvander/Documentos/GitHub/GeekUniversityPython/seçao16aula118b.py 
Saldo Inicial
saldo de 150.0 do titular Angelina com limite 1500
saldo de 300 do titular Felicity com limite 2000
Fazendo tranferência:
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
saldo de 250.0 do titular Angelina com limite 1500
saldo de 190 do titular Felicity com limite 2000

Process finished with exit code 0
"""