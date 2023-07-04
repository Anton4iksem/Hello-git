list1 = ['a', 'b', 'c', 'a', 'b']
print(list1)
a = set(list1)
print(a)
b = list(a)
print(b)


data = "John,Doe,25,USA"

# Разбить строку на список
parsed_data = data.split(',')

# Использовать f-строки для форматирования данных
name = parsed_data[0]
surname = parsed_data[1]
age = parsed_data[2]
country = parsed_data[3]
formatted_data = f"Name: {name}, Surname: {surname}, Age: {age}, Country: {country}"

print(formatted_data)
# Вывод: Name: John, Surname: Doe, Age: 25, Country: USA

# Поиск данных в ленте
feed = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
search_term = "ipsum"
if search_term in feed:
    print("Search term found in feed.")
else:
    print("Search term not found in feed.")


name = "Alice"
age = 25
height = 1.65

greeting = f"Привет, меня зовут {name}!"
description = f"Мне {age} лет и я ростом {height} метра."
