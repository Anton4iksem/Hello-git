def my_function():
    x = 10  # Локальная переменная
    print(x)

my_function()  # Вывод: 10
print(x)  # Ошибка: имя 'x' не определено


def outer_function():
    x = 10  # Закрывающая переменная

    def inner_function():
        print(x)  # Доступ к закрывающей переменной

    inner_function()

outer_function()  # Вывод: 10


x = 10  # Глобальная переменная

def my_function():
    print(x)  # Доступ к глобальной переменной

my_function()  # Вывод: 10

print(len([1, 2, 3]))  # Использование встроенной функции len()

x = 10

def my_function():
    global x
    x = 20

my_function()
print(x)  # Вывод: 20


def outer_function():
    x = 10

    def inner_function():
        nonlocal x
        x = 20

    inner_function()
    print(x)  # Вывод: 20

outer_function()