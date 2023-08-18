"""
Utilizamos esta função open() para abrir o arquivo isto não é suficiente para ler o mesmo
será necessário outra função para isto.
forma de abrir o arquivo:
    rquivo = open('aula_texto1.txt')
print(arquivo)
=> <_io.TextIOWrapper name='aula_texto1.txt' mode='r' encoding='UTF-8'>
print(type(arquivo))
=> class '_io.TextIOWrapper'>

#abre o arquivo com open()
arquivo = open('aula_texto1.txt')

# Esta função read() vai permitir a leitura do texto
print(arquivo.read())

# Esta função fecha o arquivo aberto e finalisa a conexão com sistema operacional
arquivo.close()

"""
arquivo = open('aula_texto1.txt')
print(arquivo.read())
arquivo.seek(19)
print(arquivo.read())
arquivo.close()
print(arquivo.read())

