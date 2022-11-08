def get_list():
    n = int(input())
    return sorted([int(e) for e in input().split()])


def get_result(l1, l2):
    res = abs(l1[0] - l2[0])
    i1, i2 = 0, 0

    while i1 < len(l1) and i2 < len(l2):
        res = min(res, abs(l1[i1] - l2[i2]))
        if l1[i1] < l2[i2]:
            i1 += 1
        else:
            i2 += 1
    return res


print(get_result(get_list(), get_list()))