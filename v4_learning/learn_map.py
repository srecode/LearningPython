def square(num):
    return num**2

my_nums = [1,2,3,4,5]

print(list(map(square,my_nums)))

def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'even'
    else:
        return mystring[0]

name_list = ['John','Cindy','Sarah','Kelly','Mike']

print(list(map(splicer,name_list)))