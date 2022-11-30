sq = lambda num: num ** 3

print(sq(2))

my_nums = [1,2,3,4,5]

print(list(map(lambda num: num **2, my_nums)))
print(list(filter(lambda num: num % 2 == 0, my_nums)))