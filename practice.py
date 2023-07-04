list1 = ['a']
print(id(list1))

a = 10
a = 'str'
a = True
a = 10
print(a)

my_list = ['a', 'b', 'c']
my_tuple = (my_list)
print(my_tuple)

my_list.append(4)
print(my_tuple)

def bubble_sort(arr):
    n = len(arr)

    # Проходим по списку n-1 раз
    for i in range(n - 1):
        # В каждом проходе перемещаем наибольший элемент в конец списка
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Меняем местами элементы
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Пример использования
my_list = [5, 2, 8, 12, 1]
bubble_sort(my_list)
print(my_list)


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



# Создание множества квадратов чисел от 1 до 5
squares_set = {x**2 for x in range(1, 6)}
print(squares_set)
# Вывод: {1, 4, 9, 16, 25}

# Создание множества четных чисел от 1 до 10
evens_set = {x for x in range(1, 11) if x % 2 == 0}
print(evens_set)
# Вывод: {2, 4, 6, 8, 10}


class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

# Создание итерируемого объекта
my_list = [1, 2, 3, 4, 5]
my_iterable = MyIterator(my_list)

# Итерация по элементам
for item in my_iterable:
    print(item)


try:
    # Код, который может вызвать исключение
    x = 10 / 0
except ZeroDivisionError:
    # Обработка исключения ZeroDivisionError
    print("Деление на ноль")
except Exception as e:
    # Обработка других исключений
    print("Произошла ошибка:", str(e))


def outer_function():
    x = 10  # Закрывающая переменная

    def inner_function():
        print(x)  # Доступ к закрывающей переменной
        

    inner_function()

outer_function()  # Вывод: 10

def outer_function():
    x = 10

    def inner_function():
        nonlocal x
        x = 20

    inner_function()
    print(x)  # Вывод: 20

outer_function()

my_list = [1, 2, 3]
print(dir(my_list))


