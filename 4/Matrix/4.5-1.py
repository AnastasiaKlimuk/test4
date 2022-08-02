rows = int(input())
cols = int(input())
matrix = [[0]*rows for _ in range(cols)]

for i in range(rows):
    for j in range(cols):


for r in range(rows):
    for c in range(cols):
        print(matrix[c][r], end=' ')
    print()
print()
