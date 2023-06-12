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


def lesson_13():
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


lesson_13()
