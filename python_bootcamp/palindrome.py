# Write a Python function that checks whether a word or phrase is palindrome or not.

# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, 
# e.g., madam,kayak,racecar, or a phrase "nurses run". Hint: You may want to check out the 
# .replace() method in a string to help out with dealing with spaces. Also google search how to 
# reverse a string in Python, there are some clever ways to do it with slicing notation.

def palindrome(s):
    if s == s[::-1]:
        print (f"'{s}' is a palindrome")
    else:
        print(f"'{s}' is not a palindrome")

palindrome('kayak')