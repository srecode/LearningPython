def return_all_even_numbers_from_list(num_list):
    """
    This function takes num_list list and returns all
    even numbers from that list
    :param num_list:
    :return: even_numbers[] with even numbers from the list
    """
    even_numbers = []

    for num in num_list:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            pass

    return even_numbers

print(return_all_even_numbers_from_list([1,2,3,4,5,6,7,8,9,10]))