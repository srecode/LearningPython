def ran_check_bool(num, low, high):
    if num in range(low, high):
        return True
    else:
        return False

print(ran_check_bool(7, 2 ,5))