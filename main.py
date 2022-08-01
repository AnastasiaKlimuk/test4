n = int(input())
m = int(input())
l = [[0]*m for _ in range(n)]
for i in range (n):
    for j in range(m):
        l[i][j] = input()
for c in range(n):
    for r in range(m):
        print(l[c][r], end=' ')
    print()

#
