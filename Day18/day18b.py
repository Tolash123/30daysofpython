# Lambda
x = lambda a: a+10
print(x(5))

x = lambda a,b,c: a+b+c
print(x(5,6,2))

def prod_n(num):
    return lambda a: a*num
output_triple=prod_n(3)
output_double=prod_n(2)
print(output_double(2))

# map function
lst = [2,4,6,8,10]
final_lst=list(map(lambda x: x**2,lst))
print(final_lst)

lst_animals=['dog','cat','rabbit']
upper_lst= list(map(lambda a: str.upper(a), lst_animals))
print(upper_lst)

# Filter function
def check_even(num):
    return num % 2==0

nums =[1,2,3,4,5,6,7,8]
print(list(filter(check_even,nums)))

# args and **kwargs
# For args
def my_func(a=0,b=0,c=0,d=0,e=0):
    return sum((a,b,c,d,e))*.05

print(my_func(40,60,20))

def my_func(*args):
    return sum((args))*.05
print(my_func(40,60,20))

def myfunc(*b):
    return sum((b))*.05
print(my_func(40,60,20))

def myfunc1(*args):
    total = 0
    for i in args:
        total = total+i
    print(total)
myfunc1(2,3,4,5)

# **kwargs
def myfunc(**kwargs):
    if 'fruits' in kwargs:
        print(f"My favorite fruit is {kwargs['fruit']}")
    else:
        print("i don't like fruit")
myfunc(fruit='pineapple')
