def check_even_list(num_list):
    """
    This function tests if the given list has any even numbers
    If list has even one even number it returns True
    else it returns Flase
    :return: True in case of even number in the list, False if all the
    numbers are false
    """
    for num in num_list:
        if num % 2 == 0:
            return True
        else:
            pass

    return False

print(check_even_list([1,2,3]))

print(check_even_list([1,1,3]))