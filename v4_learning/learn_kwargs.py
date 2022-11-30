def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print(f"My favorate fruit is {kwargs['fruit']}")
    else:
        print("I don't like fruits")


myfunc(fruit='Apple')

