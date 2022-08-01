n = int(input())
matrix = []
total = 0
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

for j in range(n):                     # заполняем главную диагональ единицами, а побочную двойками
    total = total + matrix[j][j]

print(total)