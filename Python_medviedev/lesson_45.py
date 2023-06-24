# Работа с файлами (открытие) в Python 3 - file openning
file = open('text.txt', 'r') # если открыть его с 'r' и файла нету то будет ошибка 
print(file.closed) # true - файл закрыт, false - файл открыт
print(file.name)
print(file.mode)
file.close() # закрыть файл нужно обязатольно закрывать потому что не сохраняться изменения

print(file.closed)

file = open('text.txt', 'w') # если файла не существует то опен с 'W' создаст его, если он был, и была какя то информация, то удалит её всю
file.close()

file = open('text.txt', 'a') # открывает файл на дозапись, предыдущая информация отсаётся, если файла не сухествет - создаёт его
file.close()

file = open('text.txt', 'rb') # rb Открывает файл для чтения, записи, дозаписи
file.close()

file = open('text.txt', 'r+') # rb+ Открывает файл для чтения, записи
file.close()

with open('text.txt', 'r') as file:
    print(file.closed)

print(file.closed)