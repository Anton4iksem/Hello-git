def lesson_21():  # Комментарии ctrl+/

    list1 = [i for i in range(8) if i % 2 == 0]
    print(list1)
    '''
    rere errere rere
    '''
# lesson_21()


def lesson_22():  # Функции
    print('kva')

# lesson_22()
# lesson_22()
# lesson_22()


def lesson_23(name, message):  # Нумерованные аргументы
    print('hi,', name, '!')
    print(message)


name1 = 'Anton'
message1 = 'kva'


# lesson_23('Anton', 'kva')
# lesson_23(name1, message1)


message = 'hello'


def lesson_24_1():  # Область видимости переменных
    # message = 'hello'
    print(message)


def lesson_24_2():
    print(message)

# print(message)
# lesson_24_1()
# lesson_24_2()


def lesson_25(s, t):  # Возврат значения функции
    v = int(s / t)
    # print('V = ', v)
    return v


v1 = lesson_25(100, 20)
v2 = lesson_25(60, 20)
# print(lesson_25(20, 20))
# print(v1, v2)


def lesson_26(name, sex, age):  # Именованные аргументы функции
    card = []
    card.append(name)
    card.append(sex)
    card.append(age)
    return card


manager = lesson_26(name='Anton', sex='M', age=25)
# print(manager)
# print('Name:', manager[0])
# print('Sex:', manager[1])
# print('Age:', manager[2])

manager = lesson_26('Anton', age=25, sex='M')
# print(manager)
# print('Name:', manager[0])
# print('Sex:', manager[1])
# print('Age:', manager[2])


def lesson_27(name=0, sex=0, age=0):  # Аргументы со значением по умолчанию - они всегда в конце
    card = []
    card.append(name)
    card.append(sex)
    card.append(age)
    return card


manager = lesson_27(name='Anton', sex='M')
manager1 = lesson_27()
# print(manager)
# print('Name:', manager[0])
# print('Sex:', manager[1])
# print('Age:', manager[2])

# print('Name1:', manager1[0])
# print('Sex1:', manager1[1])
# print('Age1:', manager1[2])


def lesson_28(*args):  # Неопределенное количество аргументов
    sum = 0
    for i in args:
        sum += i
    return sum

# print(lesson_28(2))
# print(lesson_28(5, 9))
# print(lesson_28(5, 9, 6, 7))


def lesson_29(a, b):  # Анонимные функции lamda
    return a + b

# print(lesson_29(5, 6))

def sum(a, b=8): return a + b

sum1 = lambda *args: args

# print(sum(1))
# print(sum1(1, 8, 9, 17))


def lesson_30():  # Срезы строк и списков
    stroka = 'Hello world!'
    podstroka = stroka[0:4]
    podstroka1 = stroka[:4]
    podstroka2 = stroka[2:]
    podstroka3 = stroka[::2]
    # print(podstroka)
    # print(podstroka1)
    # print(podstroka2)
    # print(podstroka3)

    list1 = [1, 2, 3, 4, 5]
    podlist = list1[0:3]
    # print(podlist)

lesson_30()
