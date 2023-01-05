def new_decorator(func):
    def wrap_func():
        print("Code would be here, before executing func()")

        func()

        print("Code will executed after func()")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("This function is needed for decorator")

# func_needs_decorator()

# func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()