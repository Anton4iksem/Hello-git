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

lesson_14_example()
