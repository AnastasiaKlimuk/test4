my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]

total = 0
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        total += my_list[i][j]
print(total)
print()

total1 = 0
for row in my_list:
    for elem in row:
        total1 += elem
print(total1)
print()

total2 = 0
for row in my_list:      # в один цикл
    total2 += sum(row)
print(total2)