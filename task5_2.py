my_f = open("my_file_tugutov.txt", "r")

n = 1
for line in my_f:

    print('В строке ', n,' содержится ', len(line), 'символов') #не нашел, была ли на уроках функция len()
    n = n + 1

print('В файле содержится', n-1, 'строк')
