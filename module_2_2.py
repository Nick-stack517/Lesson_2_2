print('Введите три целых числа,')
first = int(input('Ввведите первое число: '))
second = int(input('Ввведите второе число: '))
third = int(input('Ввведите теретье число: '))
if first == second and second == third:
    print('3')
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)
# print('Конец проги')
