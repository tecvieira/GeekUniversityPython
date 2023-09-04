"""
Embora a área de um círculo se calcule geralmente com o raio, que é metade do diâmetro,
a área também se pode encontrar diretamente pelo comprimento do diâmetro com a equação
da área igual a 1/4 * pi * diâmetro ao quadrado.

área = raio² * 3.141592
"""
print('Calcule área do circulo:')
raio = int(input('Informe tamanho do raio: '))
print('Utilizando a formula do diametro:')
diametro: int = raio * 2
area = ((1/4) * 3.141592) * (diametro ** 2)
print(f'{area}')
print('Utilizando a formula do raio')
area2 = 3.141592 * (raio ** 2)
print(f'{area2}')
