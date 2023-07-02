import random

list1 = []
max_numbers = []
min_numbers = []
l = int(input('List length: '))

def fill_and_sort():
    for i in range(l):
        number = random.randint(1, 10)
        list1.append(number)
    print(list1)

    list1.sort()
    print(list1)

# fill_and_sort()

    
def max_values():
    max_value = float('-inf') # начальное значение максимального числа, задаем отрицательную бесконечность
    for i in list1:
        if i > max_value:
            max_numbers = [i] # найдено новое максимальное число
            max_value = i
        elif i == max_value:
            max_numbers.append(max_value) # найдено еще одно максимальное число
    print(max_numbers)


def min_values():
    min_value = float('inf')
    for i in list1:
        if i < min_value:
            min_numbers = [i]
            min_value = i
        elif i == min_value:
            min_numbers.append(min_value)
    print(min_numbers)


# fill_and_sort()
# max_values()
# min_values()
