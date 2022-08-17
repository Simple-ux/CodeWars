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

