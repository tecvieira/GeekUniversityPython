reais = list() # lista original formada pelo usuário
reais2 = list() # lista produzida com valores ao quadrado da lista original.
n = 1
while n <= 10:
    num = float(input(f'Informe o {n}º número real:  '))
    reais.append(num) # adiciona um elemento a lista
    n += 1
print(reais) # lista com elementos informados pelo usuário
for elemento in reais:
    reais2.append(elemento ** 2) # Eleva o elemento ao quadrado
print(reais2) # lista formada com o quadrado dos números da lista anterior
