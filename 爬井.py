i = 20
#井的多少米
b = 3
# 白天3米
y = 2
# 晚上调2米
num = 0
# 天数
g = 0
# 爬多少米
while True:
    num += 1
    g = g + b
    if g >=i:
        break
    g = g - y

print(num)
