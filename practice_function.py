def say_hello(name="Ram"):
    print(f"Hello {name}")

say_hello("Sam")
say_hello()

def add_num(num1, num2):
    return num1 + num2

result = add_num(12,21)
print(result)

#functions with Logic
def even_check(number):
    return number % 2 == 0

print(even_check(20))

def check_even_list(number_list):
    even_list = []
    for num in number_list:
      if num % 2 == 0:
        even_list.append(num)
      else:
        pass
    return even_list
print (check_even_list([1,2,3,8,20,32,41]))

#Return Mutiple Items

stock_prices = [('AAPL', 178),('AMZN', 3330), ('TSLA', 1100),('ASML', 700)]

def stock_retunrs(stock_prices):
    for tiker,price in stock_prices:
        print(f"With 10% return on {tiker} it will be {price + (0.1*price)}")
        # return tiker
        # return (f"with 10% return on {tiker} {price + (0.1*price)}")

# print(stock_retunrs(stock_prices))
stock_retunrs(stock_prices)  

#Employee of the month

work_hours = [('Sam', 1000), ('Cam', 2000),('Dan', 400),('Carl', 600)]

def employee_of_the_year(work_hours):
    num_hours = 0
    emp_name = ''
    for name, hours in work_hours:
        if num_hours < hours:
            num_hours = hours
            emp_name = name
        else:
            pass
    return emp_name, num_hours

# print(employee_of_the_year(work_hours))

name, hours = employee_of_the_year(work_hours)
print(name)
print(hours)