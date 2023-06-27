#  Работа с файлами (чтение) 
with open(r"B:\GIT\project1\Python_medviedev\text.txt", 'r') as file:
   text = file.read()  # возвращает содержимое файла в виде одной строки
print(text)

with open(r"B:\GIT\project1\Python_medviedev\text1.txt", 'r') as file:
   for line in file:
      print(line) 

with open(r"B:\GIT\project1\Python_medviedev\text2.txt", 'r') as file:
   list = file.readlines() # возвращает в виде списка но с \n
print(list)

with open(r"B:\GIT\project1\Python_medviedev\text2.txt", 'r') as file:
   list = file.read()
   list = list.splitlines() # возвращает в виде списка безс \n
print(list)