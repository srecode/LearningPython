def square(num):
    return num**2

my_nums = [1,2,3,4,5]

# for items in map(square, my_nums):
#     print(items)

#or
print(list(map(square,my_nums)))

def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

mystring = ['Sam', 'Ram', 'Isa', 'Kian']

print(list(map(splicer,mystring)))

# print(splicer(mystring))

def find_even(num):
    return num % 2 == 0

my_nums = [1,2,3,4,5,6,7,8,9,10]

print(list(filter(find_even,my_nums)))


def tripple(num):
    results = num ** 3
    return results

print(tripple(3))

#Converint above function into lambda expression 

my_tripple = lambda num: num ** 3    

print(my_tripple(4))

my_list1 = [2,3,4,5,6]

print(list(map(lambda num:num**3,my_list1)))

print(list(filter(lambda num:num%2==0,my_list1)))

print(list(map(lambda first_l: first_l[::-1], mystring)))