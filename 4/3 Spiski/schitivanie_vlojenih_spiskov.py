n = 4                    # количество строк (элементов)
my_list = []
for _ in range(n):
    elem = [int(i) for i in input().split()]   # создаем список из элементов строки
    my_list.append(elem)
print(my_list)


n = 4
my_list1 = []
for _ in range(n):
    elem = [int(i) for i in input().split()]
    my_list1.extend(elem)
print(my_list1)