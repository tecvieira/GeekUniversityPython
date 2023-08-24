"""import time

def divisores(num):
    for i in range(1, int(num/2+1)):
        if num % i == 0:
           yield i
    yield num

inicio = time.time()

d = divisores(10)
[print(i) for i in d]

print("Fim da execução: %s segundos" % round((time.time() - inicio),2))
"""
