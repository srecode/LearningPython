"""
MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'
"""
def master_yoda(arg1):
    given_word = arg1.split()
    return ' '.join(given_word[::-1])

print(master_yoda('I am home'))
print(master_yoda('We are ready'))