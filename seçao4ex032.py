def soma_posicao(num):
    antecessor = (num * 2) - 1
    sucessor = (num * 3) + 1
    return antecessor + sucessor


print(f'Esta é a soma solicitada: {soma_posicao(int(input("Informe um número: ")))}')
