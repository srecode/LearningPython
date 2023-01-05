from collections import Counter

# lst = [1,2,3,4,51,2,3,4,1,2,31,2,334,4,56,43,2,2,2,2,2,1,1,1,1,4,5,5,56,64,3,2,3343]
s = 'How many times does each word show up in this sentence word times each each word word'
c = Counter(s.split())
print(c.most_common(1))
print(list(c))
