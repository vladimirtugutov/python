f_1 = open("my_file_tugutov.txt", 'w')
stroka = 'a'
while stroka != '':
    stroka = input('Введите данные для записи в файл:')
    f_1.write(stroka)
    f_1.write("\n")
