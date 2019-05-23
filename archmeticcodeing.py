from functools import reduce

list_1 = ['A', 'B', 'C', 'D']
list_2 = [0.1, 0.4, 0.2, 0.3]
dict_1 = {k: v for k, v in zip(list_1, list_2)}
str_2 = "CADACDB"


# 编码
def arithencode(str_1):
    # print(dict_1)
    lowlevel = 0.0
    highlevel = 1.0

    for i in str_1:
        delta = highlevel - lowlevel

        lowlevel_1 = lowlevel + delta * float(getSign(i, "low"))

        highlevel = lowlevel + delta * float(getSign(i, "high"))
        lowlevel = lowlevel_1
        # print(i,lowlevel,highlevel)
    return lowlevel


# 解码
def arithdecode(code):
    lowlevel = 0.0
    highlevel = 1.0
    delta = highlevel - lowlevel
    m = str(code)
    list_p = []
    for i in m[2:]:
        # 精度控制很重要
        lowA = round(lowlevel + delta * float(getSign('A', "low")), len(m) + 1)
        highA = round(lowlevel + delta * float(getSign('A', "high")), len(m) + 1)
        lowB = round(lowlevel + delta * float(getSign('B', "low")), len(m) + 1)
        highB = round(lowlevel + delta * float(getSign('B', "high")), len(m) + 1)
        lowC = round(lowlevel + delta * float(getSign('C', "low")), len(m) + 1)
        highC = round(lowlevel + delta * float(getSign('C', "high")), len(m) + 1)
        lowD = round(lowlevel + delta * float(getSign('D', "low")), len(m) + 1)
        highD = round(lowlevel + delta * float(getSign('D', "high")), len(m) + 1)
        if lowA <= float(code) < highA:
            n = 'A'
        elif lowB <= float(code) < highB:
            n = 'B'
        elif lowC <= float(code) < highC:
            n = 'C'
        else:
            n = 'D'
        list_p.append(n)
        '''
        print(lowlevel + delta * float(getSign('A', "low")), lowlevel + delta * float(getSign('A', "high")))
        print(lowlevel + delta * float(getSign('B', "low")), lowlevel + delta * float(getSign('B', "high")))
        print(lowlevel + delta * float(getSign('C', "low")), lowlevel + delta * float(getSign('C', "high")))
        print(lowlevel + delta * float(getSign('D', "low")), lowlevel + delta * float(getSign('D', "high")))
        '''
        lowlevel_1 = lowlevel + delta * float(getSign(n, "low"))
        highlevel = lowlevel + delta * float(getSign(n, "high"))
        lowlevel = lowlevel_1
        delta = highlevel - lowlevel
    print(list_p)


# 辅助函数
def add(x, y):
    return x + y


def getSign(n, sign, kw=dict_1):
    listd1 = list(kw.keys())
    listd2 = list(kw.values())
    if n == listd1[0]:
        if sign == "low":
            return 0.0
        else:
            return listd2[0]
    else:
        if sign == "low":
            return reduce(add, listd2[0:listd1.index(n)])
        if sign == "high":
            return reduce(add, listd2[0:listd1.index(n) + 1])


if __name__ == "__main__":
    # print(getSign('A',"high"))
    print(arithencode(str_2))
    print(list(str_2))
    arithdecode(0.5143876)
