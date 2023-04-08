# Задача 3. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти(x и y).
# 1 -> x > 0, y > 0

def GetInteger(message):
    check_int = True
    while check_int:
        try:
            number = int(input())
            check_int = False
        except:
            print(f"Введено не целое число. Повтори ввод.\n{message}", end='')
    return number


def GetQuarter(message):
    check_input = True
    while check_input:
        print(f"{message} ", end='')
        quarter = GetInteger(message)
        if quarter >= 1 and quarter <= 4:
            check_input = False
        else:
            print(f"{quarter} -> Нет такой четверти.")
    return quarter


def GetResult(quarter):
    valueSign = [">", ">"]
    if quarter == 2 or quarter == 3:
        valueSign[0] = "<"
    if quarter == 3 or quarter == 4:
        valueSign[1] = "<"
    return valueSign


def PrintResult(quarter, valueSign):
    print(f"{quarter} -> x {valueSign[0]} 0, y {valueSign[1]} 0")

quarter = GetQuarter("Введите номер четверти:")
valueSign = GetResult(quarter)
PrintResult(quarter, valueSign)