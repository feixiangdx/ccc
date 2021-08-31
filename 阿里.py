def c():
    lst = [21, 21, 21, 56, 56, 56, 56, 56, 56, 56, 56, 56, 10, 10, 10]
    dict = {}
    for item in lst:
        if item not in dict:
            dict[item] = 1
        else:
            dict[item] = dict[item] + 1
    return dict


print(c())
