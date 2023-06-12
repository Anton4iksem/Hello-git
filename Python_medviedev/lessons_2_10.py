def lesson_2():  # числа
    print(5 + 5)
    print(5 / 3)
    print(5 // 3)  # убрать остаток от деления
    print(5 % 2)  # возвращает остаток от деления
    print(5 ** 2)  # возведение в степень

# lesson_2()


def lesson_3():  # переменные
    x = 5
    y = 7
    print(x - y)

# lesson_3()


def lesson_4():  # строки
    a = "Jack"
    b = "White"
    print(a + " " + b)
    print(a*2)

# lesson_4()


def lesson_5():  # вывод на экран print()
    print("Hello world!")
    name = "Anton"
    print("My name is", name)

# lesson_5()


def lesson_6():  # экранирование
    print("Can't stop")
    print('Can\'t stop')  # \ экранирует следующий символ
    print("rhcp - \"by the way\"")
    print("ku\nku ku\nku ku")  # \n перенос на новую строку (как enter)
    print("ku\top")  # \t табулирование

# lesson_6()


def lesson_7():  # сырые строки (raw strings)
    print("B:\non_lol")
    # r перед строкой - можно использовать любые спец. символы
    print(r'B:\non_lol')


# lesson_7()


def lesson_8():  # преобразование типов
    a = '2' + '3'
    b = 5
    print(a)
    print(b)
    c = int("5") + 4  # int число
    print(c)
    d = str(5) + "6"  # str строка
    print(d)

# lesson_8()


def lesson_9():  # boolean логический тип ланных
    a = bool(5)
    b = bool(100)
    c = bool(0)
    d = bool(-1)
    print(a, b, c, d)
    e = bool("Jack")
    f = bool("64")
    g = bool("")
    print(e, f, g)

# lesson_9()


def lesson_10():  # операторы сравнения
    # > < >= <= !+ ==
    a = 1 > 2
    b = 3 < 5
    c = 3 == 3
    print(a, b, c)
    d = 'a' < 'b'
    e = 'e' > 'E'
    print(d, e)

#lesson_10()
