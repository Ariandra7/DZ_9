nunber_one = int(input('Введите число: '))
number_two = int(input('Введите число: '))

try:
    result = nunber_one / number_two
except ZeroDivisionError:
    print('На ноль делить нельзя!')
else:
    print(f"Результат деления: {result}")
