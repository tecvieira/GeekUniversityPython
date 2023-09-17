"""
Métodos mágicos sao os métodos que utilizam Dunder.
Dunder => Double Underscore
dunder init => __init__
dunder repr => __repr__
__repr__ => representa o objeto na saída
Testando saídas sem __repr__ o resultado é apenas o endereço de memória alocada para cada livro:

<__main__.Livros object at 0x7f03dfa1b250>
<__main__.Livros object at 0x7f03dfa1b390>

Testando saídas com __repr__ o resultado é representado:

livro1 =>   Python Rocks escrito por Geek University
livro2 =>  Inteligência Artificial com Python escrito por Geek University

Dunder __str__ utilizado para fazer representação do objeto para o usuário final.
Testando saídas com __str__ e __repr__ juntos a prioridade sempre será do dunder str
 Ex:        def __str__(self):
                return self.titulo
Saídas com dunder str:
Obs.: Não importa a ordem na execução a prioridade será para dunder str

livro1 => Python Rocks
livro2 => Inteligência Artificial com Python

Testando len e del

-=-=-=-=-=-=-=-=-=-=
Python Rocks
Inteligência Artificial com Python
Python Advanced
-=-=-=-=-=-=-=-=-=-=
400
350
-=-=-=-=-=-=-=-=-=-=
    def __del__(self):
        print('Um objeto do tipo livro foi deletado da memória.')
Um objeto do tipo livro foi deletado da memória.
Um objeto do tipo livro foi deletado da memória.
Um objeto do tipo livro foi deletado da memória.

"""


class Livros:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'

    def __str__(self):
        return self.titulo

    def __len__(self):
        return self.paginas

    def __add__(self, outro):
        return f'{self} - {outro}'

    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ' '
            for n in range(outro):
                msg += ' ' + str(self)
                return msg
        return 'Não posso multiplicar'

    def __del__(self):
        print('Um objeto do tipo livro foi deletado da memória.')


livro1 = Livros('Python Rocks', 'Geek University', 400)
livro2 = Livros('Inteligência Artificial com Python', 'Geek University', 350)

print('-=' * 10)
print(livro1)
print(livro2)

print('-=' * 10)
print(len(livro1))
print(len(livro2))
print('-=' * 10)
print(livro1 + livro2)
print('-=' * 10)
print(livro1 * 3)
