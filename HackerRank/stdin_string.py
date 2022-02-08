def num_string():
    n = int(input())
    i = ""
    for num in range(1,n+1):
      i += str(num) + ''
    return i

print(num_string())