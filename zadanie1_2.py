# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
t = int(input('Введите время в секундах: '))  # просим пользователя ввести время в секундах
hours = t // 3600
hours_ostatok = t % 3600
minutes = hours_ostatok // 60
minutes_ostatok = int(hours_ostatok % 60)
print(f"{hours:02.0f}:{minutes:02.0f}:{minutes_ostatok:02.0f}")

