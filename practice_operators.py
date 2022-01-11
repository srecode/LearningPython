# for i in range(0,13,3):
#     print(i)

# print(list(range(0,20,5)))

# mylist = list(range(0,31,5))

# print(mylist)

# indexing the string 

# make_index = 0
# word = 'Hello World'

# for i in word:
#     make_index += 1
#     print(make_index, i)

#enumerate 

# word = 'Hello World'

# for index, item in enumerate(word):
#     print(index,item)

#zip function 

mylist1 = [1,2,3,4]
mylist2 = ['a','b','c','d']
mylist3 = ['food', 'water', 'fire', 'air']
# for i in zip(mylist1,mylist2,mylist3):
#     print(i)

print(list(zip(mylist1,mylist2,mylist3)))