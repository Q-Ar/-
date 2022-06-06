import numpy as np
import Number2 as kurs

print("Выберите метод считывания данных.\n1. Из текстового фала\n2. Из программы")
n3 = input()
if n3 == "1":
    with open('matrixA.txt') as f:
        myA = [list(map(float, row.split())) for row in f.readlines()]
    with open("matrixB.txt") as f:
        for line in f:
            myB = [float(x) for x in line.split()]

elif n3 == "2":
    myA = [
        [1.0, -2.0, 3.0, -4.0],
        [3.0, 3.0, -5.0, -1.0],
        [3.0, 0.0, 3.0, -10.0],
        [-2.0, 1.0, 2.0, -3.0]
    ]

    myB = [
        2.0,
        -3.0,
        8.0,
        5.0]
else:
    print("Введено неверное значение.")
    quit()

myA1 = np.array(myA, int)
myB1 = np.array([[myB[0]], [myB[1]], [myB[2]], [myB[3]]], int)


# --- end of исходные данные

# --- вывод системы на экран
def FancyPrint(A, B, selected):
    for row in range(len(B)):
        print("(", end='')
        for col in range(len(A[row])):
            print("{1:6.2f}{0}".format(" " if (selected is None
                                               or selected != (row, col)) else "*", A[row][col]), end='')
        print(f") * (X{row + 1}) = ({B[row]:6.2f})")


# --- end of вывод системы на экран

# --- перемена местами двух строк системы
def SwapRows(A, B, row1, row2):
    A[row1], A[row2] = A[row2], A[row1]
    B[row1], B[row2] = B[row2], B[row1]


# --- end of перемена местами двух строк системы

# --- деление строки системы на число
def DivideRow(A, B, row, divider):
    A[row] = [a / divider for a in A[row]]
    B[row] /= divider


# --- end of деление строки системы на число

# --- сложение строки системы с другой строкой, умноженной на число
def CombineRows(A, B, row, source_row, weight):
    A[row] = [(a + k * weight) for a, k in zip(A[row], A[source_row])]
    B[row] += B[source_row] * weight


# --- Проверка
def exam(A, B, X):
    X = np.array([[X[0]], [X[1]], [X[2]], [X[3]]], int)
    res = A.dot(X)
    print("Проверка:")
    for i in range(len(res)):
        print(f"{res[i]} = {B[i]} - {(res[i] == B[i])}")


# --- end of Проверка

# --- Запись в файл
def rec(X):
    file = open("result.txt", "w")
    for i in range(len(X)):
        file.write(f"{X[i]:.2}\n")
    file.close()


# --- end of Запись в файл


# --- end of сложение строки системы с другой строкой, умноженной начисло

# --- решение системы методом Гаусса (приведением к треугольному виду)
def Gauss(A, B):
    column = 0
    while column < len(B):
        print("Ищем максимальный по модулю элемент в {0}-м столбце:".format(column + 1))
        current_row = None
        for r in range(column, len(A)):
            if current_row is None or abs(A[r][column]) > abs(A[current_row][column]):
                current_row = r
        if current_row is None:
            print("решений нет")
            return None
        FancyPrint(A, B, (current_row, column))
        if current_row != column:
            print("Переставляем строку с найденным элементом повыше:")
            SwapRows(A, B, current_row, column)
            FancyPrint(A, B, (column, column))
        print("Нормализуем строку с найденным элементом:")
        DivideRow(A, B, column, A[column][column])
        FancyPrint(A, B, (column, column))
        print("Обрабатываем нижележащие строки:")
        for r in range(column + 1, len(A)):
            CombineRows(A, B, r, column, -A[r][column])
        FancyPrint(A, B, (column, column))
        column += 1
    print("Матрица приведена к треугольному виду, считаем решение")
    X = [0 for b in B]
    for i in range(len(B) - 1, -1, -1):
        X[i] = B[i] - sum(x * a for x, a in zip(X[(i + 1):], A[i][(i + 1):]))
    print("Получили ответ:")
    print("\n".join("X{0} =  {1:.2f}".format(i + 1, x) for i, x in
                    enumerate(X)))
    exam(myA1, myB1, X)
    rec(X)
    return X


# --- end of решение системы методом Гаусса (приведением к треугольному виду)
print("Исходная система:")
FancyPrint(myA, myB, None)
print("Решаем:")
Gauss(myA, myB)
kurs.graf()  # Построение графика(номер 2)
