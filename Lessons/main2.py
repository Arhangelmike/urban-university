
def test():
    a, b = 2, 3
    print(a, b)


def test2():
    aa = 1
    bb = 2
    cc = 3
    print(aa, bb, cc)


def test3(aaa, bbb):
    print(aaa, bbb)


def test4(*params):
    print(*params)


test()
test2()
test3(2, 3)
test4(1, 2, 3, 4)
