sum = 0


def c(n):
    if n == 1:
        return 1
    return n * c(n - 1)


for i in range(1, 21):
    print(i, '!=', c(i))
    sum = sum + c(i)
print("总和为：", sum)
