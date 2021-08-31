# info = {"苹果": 32.8, "香蕉": 22, "葡萄": 15.5}
# c = input("请输入水果名称:")
# if c in info.keys():
#     print(info[c])

Friuts = {"苹果": 12.3, "草莓": 4.5, "香蕉": 6.3, "葡萄": 5.8,
          "橘子": 6.4, "樱桃": 15.8}
m = []
info = {
    "小明": {"Friuts": {"苹果": 4, "草莓": 13, "香蕉": 10}, "money": 0},
    "小刚": {"Friuts": {"葡萄": 19, "橘子": 12, "樱桃": 30}, "money": 0}
}
money = 0
name = input("输入名字")
for i in info[name]["Friuts"].keys():
    money += Friuts[i] * info[name]["Friuts"][i]
print(money)
m.append(money)
info[name]["money"] = m[0]
if name == "小明":
    print(info["小明"])
else:
    print(info["小刚"])
