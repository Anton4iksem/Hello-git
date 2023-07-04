def bubble_sort(arr):
    n = len(arr)

    # Проходим по списку n-1 раз
    for i in range(n - 1):
        # В каждом проходе перемещаем наибольший элемент в конец списка
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Меняем местами элементы
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Пример использования
my_list = [5, 2, 8, 12, 1]
bubble_sort(my_list)
print(my_list)
