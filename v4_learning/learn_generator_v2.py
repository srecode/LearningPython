def genfibon(n):
    """
    Generate fibonnaci sequence up to n
    :return:
    """
    a = 0
    b = 0
    for i in range(n):
        yield a
        a,b = b, a + b

for i in genfibon(10):
    print(i)