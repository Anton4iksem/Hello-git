from functools import reduce


numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Вывод: [2, 4, 6]

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Вывод: [1, 4, 9, 16, 25]


numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Вывод: 15


fruits = ['apple', 'banana', 'orange']

# Печать элементов списка с их индексами
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Вывод:
# 0 apple
# 1 banana
# 2 orange