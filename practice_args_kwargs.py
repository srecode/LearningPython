def my_args_func(*args):
    print(args)
    return sum(args)

print(my_args_func(1,2,3,4,5,6))

#kwargs

def my_kwargs(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit is {}'.format(kwargs['veggie']))
    else:
        print("I don't have anything")

my_kwargs(fruit='apple',veggie='banana')

#args and kwargs

def my_args_kwargs(*args,**kwargs):
    print("I like {} {}".format(args[0],kwargs['veggie']))

my_args_kwargs(10,20,30,fruit='apple',food='eggs',veggie='banana')
    