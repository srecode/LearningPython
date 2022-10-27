# tying to understand how 'Try, except and finally' works.
# we don't need to put type of exception next to except

try:
    f = open('test_file', 'r')
    f.write("Write this line")
except TypeError:
    print("There was a type Error")
except OSError:
    print("We have OS ERORR")
finally:
    print("I always run")