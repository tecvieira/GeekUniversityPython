from collections import defaultdict # importando a função defaultdict
dicionário = defaultdict(lambda:0) # lambda é uma funçao sem nome que pode ter uma saída neste caso 0
dicionário['curso'] = 'Programação em python Essencial'
# Vai gerar a seguinte saída
print(dicionário)
#defaultdict(<function <lambda> at 0x7ff00e8dc4a0>, {'curso': 'Programação em python Essencial'})
print()
print(dicionário['outro'])
# 0 - não existe esta chave, porém será criada com o valor de lambda
print(dicionário)
# defaultdict(<function <lambda> at 0x7ff00e8dc4a0>, {'curso': 'Programação em python Essencial', 'outro': 0})