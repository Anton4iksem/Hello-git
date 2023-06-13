def lesson_21():  # Комментарии ctrl+/

    list1 = [i for i in range(8) if i % 2 == 0]
    print(list1)
    '''
    rere errere rere
    '''
# lesson_21()


def lesson_22(): #  Функции 
    print('kva')

# lesson_22()
# lesson_22()
# lesson_22()

def lesson_23(name, message): #Нумерованные аргументы
    print('hi,', name, '!')
    print(message)
name1 = 'Anton'
message1 = 'kva'


# lesson_23('Anton', 'kva')
# lesson_23(name1, message1)


message = 'hello'
def lesson_24_1(): # Область видимости переменных
    # message = 'hello'
    print(message)

def lesson_24_2():
    print(message)

print(message)
lesson_24_1()
lesson_24_2()