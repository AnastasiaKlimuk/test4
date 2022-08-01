my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]
total = 0
for row in my_list:
    for elem in row:
        total += elem
print(total)