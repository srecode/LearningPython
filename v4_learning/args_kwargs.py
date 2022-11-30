def myfunc(a,b):
    return sum((a,b)) * 0.082

print(myfunc(40,10))

def args_func(*args):
    return sum(args)

print(args_func(1,2,3,4,5))