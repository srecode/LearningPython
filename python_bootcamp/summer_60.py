# SUMMER OF '69: Return the sum of the numbers in the array, 
# except ignore sections of numbers starting with a 6 and extending to the next 9 
# (every 6 will be followed by at least one 9). Return 0 for no numbers.

# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

def summer_69(my_list):
    total = 0
    add = True
    if 6 not in my_list:
        return sum(my_list)
    else: 
        for num in my_list:
            while add:
                if num != 6:
                    total += num
                    print(total) #debug
                    break
                else:
                    print("Hi 1") #debug
                    add = False
            while not add:
                if num != 9:
                    print ("Hi 2") #debug
                    print(num) #debug
                    break
                else:
                    print("Hi 3") #debug
                    print(num) #debug
                    add = True
                    break
        return total
                    

        

    
print(summer_69([1,2,3,4,5,6,7,9,10,2,6]))

    