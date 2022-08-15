def find_outlier(integers):
    res_1 = []
    res_2 = []
    for i in integers:
        if i % 2 == 0:
            res_1.append(i)
        else:
            res_2.append(i)
    if len(res_1) < len(res_2):
        return res_1[0]
    else:
        return res_2[0]

# Tests
# print(find_outlier([2, 4, 6, 8, 10, 3]))
# print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
# print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
