# Работа с файлами (запись)
with open(r'B:\GIT\project1\Python_medviedev\test.txt', 'w')as file:
    file.write('Hello world!')  # метод write в качестве аргумента принимает строку
    file.write('Hello world!\n')
    file.write('Hello world!\n')
    file.writelines(['a', 'b\n', 'b']) # метод writelines принимает список с строчными элеменнтами
