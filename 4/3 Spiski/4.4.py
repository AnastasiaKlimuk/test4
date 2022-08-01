n = int(input())
my_list = []

for i in range(1, n+1):
    elem = [j for j in range(1, i+1)]
    my_list.append(elem)
    print(elem)