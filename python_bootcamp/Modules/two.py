#two.py

import one
# from one import func
print("Top level in two.py")

one.func()

if __name__ == '__main__':
    print("two.py being run directly")
else:
    print("two.py being imported")