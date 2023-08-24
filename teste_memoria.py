import time


def fib_lista(maximo):
    nums = []
    a, b = 0, 1
    while len(nums) < maximo:
        nums.append(b)
        a, b = b, a + b
    return nums


list_time = time.time()
for n in fib_lista(10000):
    print(n)
list_timef = time.time() - list_time
print(f'O tempo de execução foi {list_timef}')
