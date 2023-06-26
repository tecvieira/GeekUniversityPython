def eleva_z(x, z):
    num = x ** z
    print(f'O numero {x} elevado a {z}ª potência é igual a {num}')


eleva_z(x=int(input('Número da base: ')), z=float(input('Expoente da potencia: ')))