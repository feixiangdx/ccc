a = 10
sum = 0
while True:
    s = input("请输入一个数：")
    s = int(s)
    a = a - 1
    if a == 0:
        print(sum)
        break
    else:
        sum = s + sum
