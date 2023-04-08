# Задача 2. Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21
import math

def GetInteger(message):
    print(f"{message}:", end=' ')
    check_int = True
    while check_int:
        try:
            number = int(input())
            check_int = False
        except:
            print(f"Введено не целое число. Повтори ввод.\n{message}:", end=' ')
    return number

def GetPointXY(message):
    pointXY = [0, 0]
    print(message)
    pointXY[0] = GetInteger("X")
    pointXY[1] = GetInteger("Y")
    return pointXY

def GetResult(pointA, pointB):
    result = math.sqrt(pow(pointB[0] - pointA[0], 2) + pow(pointB[1] - pointA[1], 2))
    return result

def PrintResult(pointA, pointB, result):
    print(f"A {pointA}; B {pointB} -> {result:0.2f}")

pointA = GetPointXY("Введите координаты точки А (целое число):")
pointB = GetPointXY("Введите координаты точки B (целое число):")
result = GetResult(pointA, pointB)
PrintResult(pointA, pointB, result)
