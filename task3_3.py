def my_func(var_1, var_2, var_3):
    return var_1 + var_2 + var_3 - min(var_1, var_2, var_3)
arg1 = float(input('vvedite chislo 1: '))
arg2 = float(input('vvedite chislo 2: '))
arg3 = float(input('vvedite chislo 3: '))

print('summa dvukh naibolshikh chisel: ')
print(my_func(arg1, arg2, arg3))


