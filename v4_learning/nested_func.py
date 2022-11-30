name = 'Sam'
def name_func():
    name = 'Sammy'
    def hello():
        print("Hello " + name)
    hello()

name_func()
print(name)