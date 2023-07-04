try:
    # Код, который может вызвать исключение
    x = 10 / 0
except ZeroDivisionError:
    # Обработка исключения ZeroDivisionError
    print("Деление на ноль")
except Exception as e:
    # Обработка других исключений
    print("Произошла ошибка:", str(e))


try:
    # Код, который может вызвать исключение
    x = 10 / 123
except ZeroDivisionError:
    # Обработка исключения ZeroDivisionError
    print("Деление на ноль")
except Exception as e:
    # Обработка других исключений
    print("Произошла ошибка:", str(e))
else:
    # Код, который будет выполнен, если исключений не возникнет
    print("Результат:", x)
finally:
    # Код, который будет выполнен в любом случае
    print("Конец программы")
