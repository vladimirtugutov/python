number = int(input('Введите целое2 положит.число: '))
m = 1
if number < 10:
    m = number
while (number > 10):
    n = (number % 10)
    if n > m:
        m = n
    number = number // 10
if number > m:
    m = number

print('Наибольшее цифра: ', m)