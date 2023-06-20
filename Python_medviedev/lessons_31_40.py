def lesson_31(): # Методы работы со строками (создают копию и возвращают в качестве результата её измененную копию)
    string = 'Hello World!'

    print(string.find('Hell'))
    print(string.find('a'))
    print(string.rfind('d'))
    print(string.index('o'))
    # print(string.index('a'))

    print(string.replace('Hell', 'A'))
    print(string)

    # string = string.replace('Hell', 'A')
    # print(string)

    list1 = string.split(' ')
    print(list1)

    print(string.upper())
    print(string.lower())
    print(string.capitalize())

    string1 = 'kva kva kva'
    print(string1.title())

    print(string.count('l'))
    print(string.count('l', 0, 5))

    string2 = ' Hello world! '
    print(string2.strip())
    print(string2.rstrip())
    print(string2.lstrip())

    print(string.swapcase())

    string3 = ', '.join(list1)
    print(string3)


# lesson_31()

def lesson_32(): #  Методы проверки строк
    print('123'.isdigit())
    print('123a'.isdigit(), '\n')

    print('asd'.isalpha())
    print('asd1'.isalpha(), '\n')

    print('123asd'.isalnum())
    print('123asd^'.isalnum(), '\n')

    print(' \n'.isspace())
    print('123 asd'.isspace(), '\n')

    print('ASD'.isupper())
    print('ASDd'.isupper(), '\n')

    print('asd'.islower())
    print('asdA'.islower(), '\n')

    print('Hello World!'.istitle())
    print('Hello world!'.istitle(), '\n')

    print('Hello World!'.startswith('Hell'))
    print('Hello World!'.startswith('hell'), '\n')

    print('Hello World!'.endswith('d!'))
    print('Hello World!'.endswith(' d'), '\n')


# lesson_32()

def lesson_33(): # Форматирование строк
    name = 'Jack'
    last_name = 'White'
    stroka = 'My first name is ' + name + '. ' + 'My last name is ' + last_name + '.'
    print(stroka)

    stroka = 'My first name is {}. My last name is {}.'.format(name, last_name)
    print(stroka)

    stroka = 'My first name is {1}. My last name is {0}.'.format(name, last_name)
    print(stroka)

    stroka = 'My first name is {name1}. My last name is {surname}.'.format(name1 = name, surname = last_name)
    print(stroka)


# lesson_33()

def lesson_34():
    list1 = ['a', 'b', 'c']
    list1.append(10)
    print(list1)
    
    list1.insert(0, 'd')
    print(list1)

    list1.insert(10, 'f ')
    print(list1)

    list1.remove('a')
    print(list1)

    # list1.remove('1')
    # print(list1)

    x = list1.pop(1)
    print(x)
    print(list1)

    list1.pop()
    print(list1)

    print(list1.index(10))
    # print(list1.index(10, 3, 6))

    print(list1.count('a'))

    list2 = list(list1.__reversed__())
    print(list2)
    # list1.reverse()

    print(list1)

    y = list1.copy()
    print(y)

    list1.extend(y)
    print(list1)

    list1.clear()
    print(list1)

# lesson_34()

def lesson_35(): # Сортировка списков
    list1 = ['abd', 'dasd', 'cdcd', 'xc', 'op']
    # list1.sort()
    print(list1)

    # list1.sort(reverse=True)
    print(list1)

    def sort1(i):
        return i[0]

    # list1.sort(key=sort1)
    print(list1)

    def sort2(i):
        return i[-1]

    # list1.sort(key=sort2)
    print(list1)

    def sort3(i):
        return len(i)
    
    # list1.sort(key=sort3)
    print(list1)

    list2 = sorted(list1)
    print(list2)

# lesson_35()  

def lesson_36(): #  Словари (dict)
    person = {}
    print(person)
    person = {'first name':'Jack', 'last name':'White'}
    print(person)
    print(len(person))
    print(person['first name'])
    person['first name'] = 'Bob'
    print(person)
    person['age'] = 25
    print(person)

# lesson_36()

def lesson_37(): # Кортежи (tuple)
    person = ()
    print(person)
    person = ('Anton', )
    print(person)
    person = ('Anton', 'Gogo')
    print(person)
    
# lesson_37()

def lesson_38(): #Перебор словарей
    person = {'first name':'Jack', 'last name':'White', 'age':25}
    for i in person:
        print(i)
        print(person[i])

    print(person.items())
    for i in person.items():
        print(i)

    for i, j in person.items():
        print(i, j)

    print(person.keys())

    for i in person.keys():
        print(i)
    
    print(person.values())
    
    for i in person.values():
        print(i)


# lesson_38()

def lesson_39(): # Методы работы со словарями
    person = {}
    person.fromkeys(('first name', 'last name'))
    print(person)
    
    person = person.fromkeys(('first name', 'last name'))
    print(person)

    person = person.fromkeys(('first name', 'last name'), 'kva kva')
    print(person)

    print(person.get('first name'))
    print(person['first name'])

    # print(person['age'])
    print(person.get('age'))
    print(person.get('age', 'Danone'))

    print(person.pop('first name'))
    print(person)

    print(person.pop('age', 25))

    print(person.popitem())
    print(person)
    # person.popitem()

    person.setdefault('first name')
    print(person.setdefault('first name'))
    print(person)

    person.setdefault('last name', 'Boba')
    print(person.setdefault('last name', 'Boba'))
    print(person)

    person.update({'age':25, 'sex':'m'})
    print(person)

    person1 = person.copy()
    print(person1)

    person1.clear()
    print(person1)

# lesson_39()

def lesson_40(): # Множества set и frozenset
    list1 = set()
    print(list1)
    list1 = {'a', 'b', 'c', 'a', 'b'}
    print(list1)

    list2 = frozenset()
    print(list2)
    list2 = {'a', 'b', 'c', 'a', 'b'}
    print(list2)
    
lesson_40()