'''Задача 5. Квадраты в диапазоне'''

print('Задайте диапазон из двух целых чисел:')
a = int(input())
b = int(input())

for n in range(0, 100):
    for i in range(a, b + 1):
        if i**0.5 == n:
            print(i, end=" ")