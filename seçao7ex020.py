from random import randint

list1 = []
while len(list1) < 10:
    list1.append(randint(0, 50))
print(f'Os valores gerados: {list1}')
list2 = []
for n in list1:
    if n % 2 == 1:
        list2.append(n)
print(f'Os valores ímpares:{list2}')
