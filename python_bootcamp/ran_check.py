def ran_check(num, low, high):
    if num in range(low, high):
        print (f"{num} in range {low} and {high}")
    else:
        print (f"{num} not in range {low} and {high}")

ran_check(7, 2 ,5)