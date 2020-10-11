n = int(input('Введите число: '))
if n > 9:
    print('введите число меньше 10')
else:
    sum = (n * 100 + n * 10 + n) + (n * 10 + n) + n
    print(sum)