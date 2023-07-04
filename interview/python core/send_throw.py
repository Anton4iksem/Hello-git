def my_generator():
    try:
        value = yield 10  # Передаем значение 10 обратно вызывающей стороне и ожидаем входящего значения
        print("Received:", value)
        yield 20
        yield 30
    except Exception as e:
        print("Exception:", e)

gen = my_generator()

# Запускаем генератор
result = next(gen)
print("Generated:", result)  # Вывод: Generated: 10

# Отправляем значение обратно в генератор
result = gen.send(100)  # Вывод: Received: 100

result = next(gen)
print("Generated:", result)  # Вывод: Generated: 30

# Генерируем исключение в генераторе
# gen.throw(ValueError("Custom Error"))  # Вывод: Exception: Custom Error
