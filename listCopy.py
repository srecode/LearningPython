#this script is tp learn about copy and Deepcopy

import copy

def listCopy():
    orig = [1,2,3,4]
    dup = orig
    print("print Orig ") + str(orig)
    orig.append("Hello")
    print("Print dup ") + str(dup)

    cOrig = [1,2,3,4]
    Cdup = copy.copy(cOrig)
    print("print COrig ") + str(cOrig)
    cOrig.append("Hello")
    print("Print Cdup ") + str(Cdup)
    print("Print COrig after append") + str(cOrig)

listCopy()
