from itertools import count, cycle

for n in count(5):
    print(n)
    if n >= 10:
        break

print(' ')

x = 0
list = ['a', 'b', 'c', 'd']
x = cycle(list)
for i in range(len(list) * 4):
    print(next(x), end=' ')
