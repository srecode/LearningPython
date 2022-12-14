try:
    f = open('testfile', 'r')
    f.write("I am writing this to a file")
except TypeError:
    print("Hey you have a type error")
except OSError:
    print("Hey you have OSError")
finally:
    print("I always run")