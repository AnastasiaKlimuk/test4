#Способ 1
n, m = int(input()), int(input())
my_list = []
for _ in range(n):
    my_list.append([0] * m)
print(my_list)

#Способ 2
n, m = int(input()), int(input())
my_list = [0] * n
for i in range(n):
    my_list[i] = [0] * m
print(my_list)

#Способ 3
n, m = int(input()), int(input())
my_list = [[0] * m for _ in range(n)]
print(my_list)