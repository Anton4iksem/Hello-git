def lesson_41(): # Методы работы со множествами set и frozenset  - они не изменяют множества
    a = {1, 2, 3}
    print(len(a))
    # print(len(a[0])) - нельзя обратиться к элементу множества
    print(1 in a)
    print(5 in a)
    b = {2, 3, 4}
    c = {3, 4, 5}
    d = {9, 8}
    a1 = a.union(b, c) # обьединение множества а с множествами b и с
    print(a1)
    a2 = a | b | c # обьединение множества а с множествами b и с
    print(a2)
    a3 = a.intersection(b, c) # пересечение множества а с множествами b и с
    print(a3)
    a4 = a & b & c # пересечение множества а с множествами b и с
    print(a4)
    a5 = a.intersection(d)
    print(a5)
    a6 = a.difference(b ,c) # уникальные элементы множества а
    print(a6)
    a7 = a - b - c - d # уникальные элементы множества а
    print(a7)
    a8 = a.symmetric_difference(b) # уникальные элементы в двух множествах а и b, у метода только один аргумент!
    print(a8)
    a18 = a ^ b # уникальные элементы в двух множествах а и b
    print(a18)
    a9 = a.isdisjoint(b) # проверка отличаются ли полностью элементы в двух множествах true/false
    print(a9)
    a10 = a.isdisjoint(d) # проверка на идентичность true/false
    print(a10)
    a11 = a == b
    print(a11)
    e = {1, 2, 3}
    a12 = a == e 
    print(a12)
    a13 = a.issubset(b) # проверка: входят ли все эдементы множества а в множество b true/fals
    print(a13)
    a14 = a <= b  # проверка: входят ли все эдементы множества а в множество b true/false
    print(a14)
    a15 = a.issuperset(b) # проверка: входят ли все эдементы множества b в множество a true/false
    print(a15)
    a16 = a >= b # проверка: входят ли все эдементы множества b в множество a true/false
    print(a16)
    a17 = a.copy() # возвращает копию множества 
    print(a17)


# lesson_41()

def exapmple_41(a, b):
    c = a | b
    print(c)


# exapmple_41({1, 2, 3}, {2, 3, 1, 7, 8 ,8})

def lesson_42(): # Методы работы со множеством set, к frozenset - неприменимо, изменяет множество
    a = {1, 2, 3}
    b = {2, 3, 4}
    c = {3, 4, 5}
    a.update(b, c) # обьединяет множество а с множествами b и с
    print(a)
    a = {1, 2, 3} # обьединяет множество а с множествами b и с
    a |= b | c
    print(a)

    a = {1, 2, 3}
    a.intersection_update(b, c) # пересечение множества а с множествами b и с
    print(a)
    a = {1, 2, 3}
    a &= b & c # пересечение множества а с множествами b и с
    print(a)

    a = {1, 2, 3}
    a.difference_update(b, c) # уникальные элементы множества а
    print(a)
    a = {1, 2, 3} 
    a -= b | c # уникальные элементы множества а, сначала обьединение множеств b и с, а потом вычитание от множества а
    print(a)

    a = {1, 2, 3} 
    a.symmetric_difference_update(b) # уникальные элементы в двух множествах а и b, у метода только один аргумент!
    print(a)
    a = {1, 2, 3} 
    a ^= b # уникальные элементы в двух множествах а и b
    print(a)

    a = {1, 2, 3} 
    a.add(2)
    print(a)
    a.add(7) # добавляет элемент во множество=
    print(a) 

    a.remove(7) # удаляет элемент из множества
    # a.remove(71) - error
    print(a) 

    a.discard(1) # удаляет элемент из множества, если удалить несуществующий элемент то ошибки не будет как в методе remove()
    print(a)
    a.discard(11)
    print(a)

    a1 = a.pop() # удаляет "первый"(неупорядоченая коллекция - рандомно) элемент множества и возвращает его
    print(a1)
    print(a)

    b.clear() # удаляет все элементы из множества
    print(b)


lesson_42()