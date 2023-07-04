def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print("Ошибка:", str(e))


class MyCustomException(Exception):
    pass

def process_data(data):
    if not data:
        raise MyCustomException("Отсутствуют данные")
    # Дальнейшая обработка данных

try:
    process_data([])
except MyCustomException as e:
    print("Ошибка:", str(e))