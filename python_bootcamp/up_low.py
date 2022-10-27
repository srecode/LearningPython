# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output : 
# No. of Upper case characters : 4
# No. of Lower case Characters : 33

from curses.ascii import islower
from re import S

s = "Hello Mr. Rogers, how are you this fine Tuesday?"
def up_low(s):
    up = 0
    low = 0
    for i in s:
        if i.islower():
            low += 1
        elif i.isupper():
            up += 1
        else:
            pass

    return up, low

print(up_low(s))