#This script is to play woth local and global variables

eggs = 21
def spam():
    eggs = 12
    bacon()
    # print(eggs)

def bacon():
    ham = 101
    # eggs = 0
    

spam()
# print(eggs)