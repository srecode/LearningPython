import one

def func():
    print("FUNC() in two.py")

print("top level in two.py")

if __name__ == '__main__':
     print("two.py being run directly")
else:
    print("two.py is been imported")