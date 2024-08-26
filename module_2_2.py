print('Введите число для проверки')
try:
    first = int(input('first:'))
    second = int(input('second:'))
    third = int(input('third:'))
    if first == second == third:
        print(3)
    elif first != second != third:
        print(0)
    else:
        print(2)
except ValueError:
    print('Введите только числовое значение')
