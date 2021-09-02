i = 1
while i < 10:
    j = 1
    print("%d*%d=%2d" % (i, j, i * j))
    j = j + 1
    i=i+1
    if j <10:
        print("%d*%d=%2d" % (i, j, i * j))
    else:
        break
