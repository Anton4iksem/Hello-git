def my_generator():
    yield 1
    yield 2
    yield 3


# Использование генератора
my_gen = my_generator()
print(next(my_gen))  # Вывод: 1
print(next(my_gen))  # Вывод: 2
print(next(my_gen))  # Вывод: 3


my_gen = (x for x in range(1, 4))

# Использование генератора
print(next(my_gen))  # Вывод: 1
print(next(my_gen))  # Вывод: 2
print(next(my_gen))  # Вывод: 3


def infinite_generator():
    num = 0
    while True:
        yield num
        num += 1


# Использование нескончаемого генератора
my_gen = infinite_generator()
print(next(my_gen))  # Вывод: 0
print(next(my_gen))  # Вывод: 1
print(next(my_gen))  # Вывод: 2
# И так далее...
