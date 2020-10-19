
from sys import argv

script_name, выработкавчасах, ставкавчас, премия = argv

#print("Имя скрипта: ", script_name)
print("Расчет заработной платы сотрудника: ", float(выработкавчасах) * float(ставкавчас) + float(премия))
