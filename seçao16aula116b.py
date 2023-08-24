"""
Métodos de Classe (continuação da aula 116)

Testando:
user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')
Usuario.conta_usuarios()  # modo correto de acesso
user.conta_usuarios()  # modo incorreto

Métodos privados:
# Testando metodo privado, a função __gera_usuario esta sendo chamada dentro da classe Usuario
user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')
print(user._Usuario__gera_usuario()) # Forma ruim de acessar, é possível porém errada.

Métodos estáticos:
Testando metodo estático:
print(Usuario.contador)
print(Usuario.defiicao())
user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')
print(user.contador)
print(user.defiicao())

"""
from passlib.hash import pbkdf2_sha256 as cryp


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminsidade = luminosidade
        self.__ligada = False


class ContaCorrente:
    contador = 4999

    def __init__(self, numero, limite, saldo):
        self.__numero = numero
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome1 = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        return self.__valor * (100 - porcentagem) / 100


class Usuario:
    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuários no sistema.')

    @staticmethod
    def defiicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]
