# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

def master_yoda(string):
    return ' '.join(string.split()[::-1])

print(master_yoda("Hello Sir"))
print(master_yoda('We are ready'))
    