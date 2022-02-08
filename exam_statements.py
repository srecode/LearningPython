#Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'

for sts in st.split():
    if sts[0] == 's':
      print(sts)

#Use range() to print all the even numbers from 0 to 10.
for num in range(10):
    print(num)

#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
# print([num for num in range(1,50) if num % 3 == 0])
print([num for num in range(1,50) if num % 3 == 0])

#Go through the string below and if the length of a word is even print "even!"
print ([st for st in 'Print every word in this sentence that has an even number of letters'.split() if len(st) % 2 == 0])

#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for num in range(1,100):
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} FizzBuzz")
    elif num % 3 == 0:
        print(f"{num} Fizz")
    elif num % 5 == 0:
        print (f"{num} Buzz")
    
#Use List Comprehension to create a list of the first letters of every word in the string below:

print ([st[0] for st in 'Create a list of the first letters of every word in this string'.split()])

        