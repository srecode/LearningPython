def repeate_3(string):
    result = []
    for i in string:
        result.append(''.join(i*3))
    return ''.join(result)

print(repeate_3("Hello"))
print(repeate_3("Mississippi"))