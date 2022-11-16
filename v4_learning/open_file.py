def openfile():
    myfile = open('myfile.txt')
    print(myfile.read())
    myfile.seek(0) #in order to read the file again you need to seek it to 0 first for the opne files.
    print(myfile.read())
    myfile.close() # If you don't close this file, Python will complain about this if you open this file else where.
# openfile()

def open_file_with():
    """
    Best practice is to open a file "with"
    so that you don't have to explicitly close it
    once we are done using it
    :return:
    """
    with open('myfile.txt') as myfile:
        print(myfile.read())

# open_file_with()

"""
mode r is for reading
w is for writing, overwrites a file
a for append, starts from end of the file
r+ read and write 
w+ write and read, overwrites a file
"""

def open_with_mode():
    with open('new_file.txt', 'r+') as f:
        f.write("Hello I am writing to this file, opening with read+") #Created a new file
        print(f.read()) #this fails with mode 'w' and works with 'w+'

open_with_mode()