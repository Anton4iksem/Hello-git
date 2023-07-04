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


class MyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)


# Создание итерируемого объекта
my_list = [1, 2, 3, 4, 5]
my_iterable = MyIterable(my_list)

# Итерация по элементам
for item in my_iterable:
    print(item)
