'''
import random

n = int(input("Введіть кількість елементів у списку: "))

list = [random.randint(-10, 10) for _ in range(n)]

if 0 not in list:
    list[random.randint(0, n - 1)] = 0

print("Початковий список:", list)

second_list = [x for x in list if x != 0]
zero_count = list.count(0)
result = second_list + [0] * zero_count

print("Змінений список:", result)

'''


import random

n = int(input("Введіть кількість літер в імені: "))
m = int(input("Введіть кількість літер в прізвищі: "))

matrix = [[round(random.uniform(-10, 10), 2) for _ in range(n)] for _ in range(m)]

print("Початкова матриця:")
for row in matrix:
    print(row)

min_sum = float('inf')
min_row = []

for row in matrix:
    row_sum = sum(row)
    if row_sum < min_sum:
        min_sum = row_sum
        min_row = row

print("\nРядок з мінімальною сумою елементів:", min_row)
print("Сума елементів цього рядка:", round(min_sum, 2))
