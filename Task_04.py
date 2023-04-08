# Задача 4. Напишите программу, которая на вход принимает число(N),
# а на выходе показывает все чётные числа от 1 до N.
# 5 -> 2, 4
# 8 -> 2, 4, 6, 8

def GetInteger(message):
    check_int = True
    while check_int:
        try:
            number = int(input())
            check_int = False
        except:
            print(f"Условие ввода не выполнено. Повтори ввод.\n{message}", end='')
    return number

def GetNumber(message):
    check_input = True
    while check_input:
        print(f"{message} ", end='')
        number = GetInteger(message)
        if number > 0:
            check_input = False
        else:
            print(f"{number} -> Введено отрицательное число.")
    return number

def PrintResult(number):
    print(f"{number} - >", end=' ')
    for i in range(2,number + 1, 2):
        print(f"{i}", end = ' ')

number = GetNumber("Введите целое положительное число: ")
PrintResult(number)
