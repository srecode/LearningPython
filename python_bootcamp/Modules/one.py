#one.py

def func():
    print("FUNC() IN ONE.PY")

print("TOP LEVEL IN ONE.PY")
print("This")

if __name__ == '__main__':
    print("one.py ran directly")
else:
    print("one.py is imported!")