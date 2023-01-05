def gencubes(n):
    for i in range(10):
        yield i ** 3

for x in gencubes(10):
    print(x)