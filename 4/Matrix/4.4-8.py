cols = int(input())
rows = int(input())
l = [[0]*rows for _ in range(cols)]
for i in range (cols):
    for j in range(rows):
        l[i][j] = input()

#Перебор по строкам
for r in range(cols):
    for c in range(rows):
        print(l[r][c], end=' ')
    print()
print()
