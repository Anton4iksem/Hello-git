def lesson_11():  # первая программа
    a = 'jack'
    b = 'white'
    c = a + " " + b
    print("my name is", c)

# lesson_11()


def lesson_12():  # input функция ввода
    a = input("Enter something:")
    print(a)

# lesson_12()


def lesson_13():  # условные инструкции (if else)
    login = input("Who are you? ")
    if login == 'me':
        print('Correct')
        password = input('Password: ')
        if password == 'qwerty':
            print('hi!')
        else:
            print('Wrong!')
    elif login == 'friend':
        print('Hi friend!')
    else:
        print('Wrong!')
    # print('It works')


# lesson_13()

def lesson_14():  # Логические операторы or and not
    a = True and True
    b = True and False
    c = False and False
    print(a, '\n',  b, '\n', c, '\n', sep='')
    d = True or True
    e = True or False
    f = False or False
    print(d, '\n',  e, '\n', f, '\n', sep='')
    g = not False
    h = not True
    print(g, '\n',  h, '\n', sep='')
    i = 1 and 0
    j = 0 and 1
    k = 0 and 0
    l = 1 and 1
    print(i, '\n',  j, '\n', k, '\n', l, '\n', sep='')
    m = 1 or 0
    n = 0 or 0
    print(m, '\n',  n, '\n', sep='')

# lesson_14()


def lesson_14_example():

    login = input("Who are you? ")
    password = input('Password: ')
    if login == 'me' and password == 'qwerty' or login == 'friend' and password == '12345':
        print('Correct')
    else:
        print('Wrong!')

# lesson_14_example()


def lesson_15():  # Цикл while
    i = 0

    while i < 10:
        print(i)
        i += 1

# lesson_15()


def lesson_15_example():
    num = int(input('Number: '))
    i = 0
    while True:
        print(i)
        i += 1
        if i == num:
            break
    print('Number is = ', i)

    # while i < 20:
    #     i += 1
    #     if i == num:
    #         continue #перепрыгнет число которое я введу
    #     print(i)
    # print('Number is = ', i)

    # i = 10
    # while True:
    #     num = int(input('Number: '))
    #     if i == num:
    #         print('Congrats')
    #         break

# lesson_15_example()


def lesson_16():  # Списки (list)
    list = [1, 2, 'a', 'b', True, False]
    print(len(list))

    list1 = ['a', 'b', 'c', 'd']
    print(list1[0])
    print(list1[-1])

    print('a' in list1)
    print('f' in list1)

    list1[0] = 'f'
    print(list1)

    list1.append('a')
    print(list1)

    list2 = ['1', '2', '3']
    list3 = ['a', 'b', list2]
    print(list3)

    print(list3[2][1])

# lesson_16()


def lesson_17():  # Цикл for in
    list = ['a', 'b', 'c', 'd']
    for i in list:
        if i == 'b':
            print('bb')
            break
        print(i)

# lesson_17()


def lesson_17(): # Функция range
    import random
    a = list(range(10))
    print(a)

    b = list(range(random.randint(1, 10)))
    print(b)
lesson_17()