# '''
#     1.用金钱
#     2.空的购物车
#     3.有足够商品
#     4.正常购物
#         是否有这个商品
#         金钱是否足够
#             添加购物车
#
#     技术选型：
#         1.判断
#         2.循环
#         3.容器技术
#         4.输入input
#         5.打印
#     任务1：
#         10张联想优惠券，0.5
#         20张老干妈优惠券：0.6
#         10张乌江榨菜优惠券，0.9
#     最后使用优惠券来结算。
# '''
# 1.准备一个商品柜
import random

print("是否需要优惠券？1[yes],2[no]", end="")
ch = input("")
ch = int(ch)
if ch == 1:
    c = random.randint(1, 40)
    if c <= 10:
        print("恭喜你获得联想优惠券：0.5")
    elif 11 <= c <= 30:
        print("恭喜你获得老干妈优惠券：0.6")
    else:
        print("恭喜你获得乌江榨菜优惠券：0.9")
    print("温馨提示：此卷只可你使用一次")
elif ch == 2:
    print("对不起，您未获得优惠券。")
else:
    print("输入错误,不想要就滚！！！！！")
shop = [
    ["联想电脑", 4500],
    ["Mac Pc", 12000],
    ["HUA WEI WATCH", 1200],
    ["海尔洗衣机", 5000],
    ["卫龙辣条", 3.5],
    ["老干妈", 15],
    ["乌江榨菜", 1.5]
]

# 2.准备钱包
money = input("请初始化您的余额：")
money = int(money)

# 3.空格购物车
mycart = []

# 4.正常买东西

while True:
    # 展示商品
    for key, value in enumerate(shop):
        print(key, value)
    # 买东西
    chose = input("亲输入您要的商品编号：")
    if chose.isdigit():
        chose = int(chose)
        #  这个商品是否存在
        if chose > len(shop):  # len(shop) = 7
            print("该商品不存在！别瞎弄！请重新输入：")
        else:
            # 看钱够不够
            if money < shop[chose][1]:
                print("对不起，您的余额不足，穷鬼，请到其他地方购买！")
            else:
                if chose == 0 and c <= 10:
                    mycart.append([shop[0][0], shop[0][1] * 0.5])
                    money = money - shop[0][1] * 0.5
                elif chose == 5 and 11 <= c <= 30:
                    mycart.append([shop[5][0], shop[5][1] * 0.6])
                    money = money - shop[5][1] * 0.6
                elif chose == 6 and c > 30:
                    mycart.append([shop[6][0], shop[6][1] * 0.9])
                    money = money - shop[6][1] * 0.9
                else:
                    mycart.append(shop[chose])
                    money = money - shop[chose][1]
            print("恭喜，添加购物车成功！您的余额还剩：", money, "!")
    elif chose == 'q' or chose == 'Q':
        print("欢迎下次光临！")
        break
    else:
        print("输入非法！别瞎弄！请重新输入：")

# 结算,打印购物小条
print("以下是您的购物小条，请查收：")
print("----------------------------")
for key, value in enumerate(mycart):
    print(key, value)
print("您本次余额还剩：￥", money)
print("----------------------------")
