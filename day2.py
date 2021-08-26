import random

num = random.randint(0, 10)
b = 100
while True:
    a = input("请输入一个数字")  # 你输入的数字
    a = int(a)  # 把a转换成int类型
    if a == num or b == 0:  # a是你输入的数字  num是随机数  如果a等于num运行下面的代码
        if a == num:
            print("成功", a)
            break
        else:
            print("游戏结束,资金不足")
            break
    else:
        b = b - 10
        if a > num:
            print("猜的数值过大")
            print("扣除资金10块，剩余：", b)
            break
        else:
            print("猜的数值过小")
            print("扣除资金10块，剩余：", b)
