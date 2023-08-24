"""
METODOS DE iNSTÂNCIA

# testando classe produto
p1 = Produto('PlayStation4', 'VideoGame', 2300)
print(p1.desconto(50))
print(Produto.desconto(p1, 40))  # precisa passar classe e desconto

# testando classe usuario
user1 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '123456')
user2 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '654321')

print(user1.nome_completo())
print(user2.nome_completo())

print(f'Senha: {user1._Usuario__senha}') # Acesso de forma errada de um atributo de classe
print(f'Senha: {user2._Usuario__senha}') # Acesso de forma errada de um atributo de classe

"""


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


from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


nome = input('Informe seu nome: ')
sobrenome = input('Informe sobrenome: ')
email = input('Informe seu e-mail: ')
senha = input('Informe sua senha com 6 caracteres: ')
confirma_senha = input('Confirme sua senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere!')
    exit(1)

print('Usuário criado com sucesso')
senha = input('informe a senha de acesso: ')

if user.checa_senha(senha):
    print('Acesso Permitido')
else:
    print('Acesso negado!!!')
print(f'Senha User Cripitografada: {user. _Usuario__senha}')  # Acesso de forma errada

# NÃO ESTÁ EXECUTANDO CONFORME A AULA
