# my_file = open('sample.txt')
# print (my_file.read())

#new way

with open('sample.txt', mode='a') as new_file:
    new_file.write('Line four\n')
    # content = new_file.read()
    # print (content)