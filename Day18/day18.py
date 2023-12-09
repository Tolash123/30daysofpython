# Defining a function
def mom():
    print('Hello mom1')
mom()

# Accepting parameters(arguments)
def greeting(name):
    print(f'Hello {name}')
greeting('Dristol')

def summation():
    a = eval(input('Enter a number: '))
    b = eval(input('Enter a number: '))
    print(a+b)
summation()

# Using return
def add_num(n1,n2):
    return n1+n2
print(add_num(4,5))

# To show the difference between the return and print() function
def my_result(a,b):
    print(a+b)
    return a+b
my_result1 = my_result(20,20)
my_result(40,50)
print(my_result1)

# Adding logic to internal function operations

def even_check(num):
    return num % 2 == 0
print(even_check(20))

# To check if any number in a list is even
def check_even(num):
    for n in num:
        if n % 2 == 0:
            return True
        else:
            pass
        return False
print(check_even([1,5,3])) 

# To print shape
def shape():
    a = int(input('Enter row number: '))
    for i in range(a):
        print('[]'*a)
shape()

# To return all even numbers in a list

def even_list(num):
    even_num = []
    # Go through each number
    for n in num:
        # if the output is True
        if n % 2==0:
            even_num.append(n)
            print(even_num)
        else:
            pass
        
print(even_list([1,2,3,4,6,7]))

# Returning tuples for unpacking
stock_prices = [('AAPl', 200),('Goog',300),('Msft', 400)]
print(type(stock_prices))

# To print the items in the stock
for item in stock_prices:
    print(item)
# To print the stock and prices seperately
for stock, price in stock_prices:
    print(stock)
    print(price)

# To store students data
#Note: This format can be used in creating simple database 
student_data = [
    ('Alade Idris Tolani', 'Software engineering', 400),
    ('Akinfemiwa Ayodeji', 'Cyber security', 400),
    ('Onoruoiza Abdullahi', 'Information Technology', 400),
    ('Abdullahi Moryam','computer-science',400)
]

for item in student_data:
    print(item)
# To print name of student
for name,dept,level in student_data:
    print(dept,level)
