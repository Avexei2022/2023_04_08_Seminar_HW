# Задача 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и выводит название этого дня недели.
# 1 –> Понедельник
# 10 –> Нет такого дня
# 7 –> Воскресение

def GetInteger(message):
    check_int = True
    while check_int:
        try:
            number = int(input())
            check_int = False
        except:
            print(f"Введено не целое число. Повтори ввод.\n{message}", end='')
    return number

def GetDayNum(message):
    check_input = True
    while check_input:
        print(f"{message} ", end='')
        dayNum = GetInteger(message)
        if dayNum >= 1 and dayNum <= 7:
            check_input = False
        else:
            print(f"{dayNum} -> Нет такого дня.")
    return dayNum


def GetResult(dayNum):
    weekDay = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return weekDay[dayNum - 1]


def PrintResult(dayNum, dayName):
    print(f"{dayNum} -> {dayName}")


dayNum = GetDayNum("Введите цифру дня недели: ")
dayName = GetResult(dayNum)
PrintResult(dayNum, dayName)
