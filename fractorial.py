def fractorial(x):
    num = 1
    for i in range(1, x+1):
        num = i * num
    print num

fractorial(5)
