a = 10
lst = []
while a != 0:
    s = int(input("请输入一个数："))
    lst.append(s)
    a = a - 1
print(max(lst))
print(sum(lst))
print(sum(lst) / 10)
