n = int(input())
matrix = []
total = 0
counter = 0
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
    sum_row= sum(matrix[i])/n
    print(sum_row)
    if float(matrix[i][i]) > sum_row:
        counter = counter+1
    print(counter)