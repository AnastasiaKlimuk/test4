n = int(input())
p = 0
v = 0
t = 0
c = 0
mtr = [[int(i) for i in input().split()] for j in range(n)]

for i in range(n):
    for j in range(n):
        if (i < j and i < n - 1 - j):
            p = p+mtr[i][j]
        elif (i < j and i > n-1-j):
            v = v+mtr[i][j]
        elif (i > j and i > n-1-j):
            t = t+mtr[i][j]
        elif (i > j and i < n-1-j):
            c = c+mtr[i][j]
print('Верхняя четверть:', p)
print('Правая четверть:', v)
print('Нижняя четверть:', t)
print('Левая четверть:', c)
