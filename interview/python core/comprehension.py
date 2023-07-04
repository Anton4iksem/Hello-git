# Создание списка кубов чисел от 0 до 10
cubes = [x**3 for x in range(1, 11)]
print(cubes)
# Вывод:[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

cubes1 = []
for x in range(1, 11):
    x = x**3
    cubes1.append(x)
print(cubes1)

# Создание списка квадратов чисел от 0 до 9
squares = [x**2 for x in range(10)]
print(squares)
# Вывод: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Создание списка четных чисел от 0 до 9
evens = [x for x in range(10) if x % 2 == 0]
print(evens)
# Вывод: [0, 2, 4, 6, 8]

# Создание словаря, где ключами являются числа, а значениями их квадраты
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)
# Вывод: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Создание словаря, где ключами являются элементы списка, а значениями их длины
fruits = ['apple', 'banana', 'cherry']
length_dict = {fruit: len(fruit) for fruit in fruits}
print(length_dict)
# Вывод: {'apple': 5, 'banana': 6, 'cherry': 6}
