
def my_div(arg_1, arg_2):
    return arg_1 / arg_2
arg1 = float(input('vvedite delimoe: '))
arg2 = float(input('vvedite delitel: '))
if arg2 == 0:
    print('delenie na 0!!!')
else:
    print('chastnoe ot deleniya: ')
    print(my_div(arg1, arg2))


