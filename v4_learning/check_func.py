def return_true():
    return False

def use_func():
    if return_true():
        print("Yeah, this works")
    else:
        print("Nope this doesn't work")

use_func()