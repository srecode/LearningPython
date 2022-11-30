def vol(r):
    return (4/3) * 3.144 * r ** 3

print(vol(2))

def ran_check(num,low,high):
    """
    Write a function that checks whether a number is in a given range (inclusive of high and low)
    :return:
    """
    # lower = num - low
    # higher = num - high
    # print(lower)
    # print(higher)
    #
    # if higher > lower:
    #     print(f"{num} is closer to lower number {low}")
    # else:
    #     print(f"{num} is closer to higher number {high}")

    if num in range(low, high+1):
        print('{} is in the range between {} and {}'.format(num, low, high))
    else:
        print(f"{num} out of range from {low} and {high}")

ran_check(3,2,7)

# if you want the above answer in bool you can do below

def ran_bool(num, low, high):
    return num in range(low, high+1)

print(ran_bool(5,2,8))