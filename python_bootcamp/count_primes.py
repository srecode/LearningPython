def count_primes(num):

    # check for 0 or 1 input
    if num < 2:
        return 0
    # 2 or greater
    
    #Store our prime number
    primes = [2]
    # counter going up to the input num
    x = 3

    # x is going through every number in the input
    while x <= num:
        for y in range(3,x,2):
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

print(count_primes(100))
