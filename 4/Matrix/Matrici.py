
rows, cols = 3, 4      # rows - количество строк, cols - количество столбцов
matrix = [[277, -930, 11, 0],
           [9, 43, 6, 87],
           [4456, 8, 290, 7]]

#Перебор по строкам
for r in range(rows):
    for c in range(cols):
        print(matrix[r][c], end=' ')
    print()
print()

#Перебор по столбцам
for c in range(cols):
    for r in range(rows):
        print(matrix[r][c], end=' ')
    print()
print()

#ljust - добавление символов в конец для выравнивания матрицы
for r in range(rows):
    for c in range(cols):
        print(str(matrix[r][c]).ljust(6), end='')
    print()
print()

#Заполнение диагоналей матрицы
n = 8
matrix1 = [[0]*n for _ in range(n)]    # создаем квадратную матрицу размером 8×8
for i in range(n):                     # заполняем главную диагональ единицами, а побочную двойками
    matrix1[i][i] = 1
    matrix1[i][n-i-1] = 2
for r in range(n):                     # выводим матрицу
    for c in range(n):
        print(matrix1[r][c], end=' ')
    print()
print()

#Функция для вывода квадратной матрицы
def print_matrix(matrix2, n, width=1):
    for r in range(n):
        for c in range(n):
            print(str(matrix2[r][c]).ljust(width), end=' ')
        print()

#Считывание матрицы
n = int(input())
matrix3 = []
for j in range(n):
    temp = [int(num) for num in input().split()]
    matrix3.append(temp)
print(matrix3)
