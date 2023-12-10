# Write a Python function that checks whether a passed string is palindrome or not.
def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
print(palindrome('helleh'))

# Given a number N.Find Sum of 1 to N Using Recursion
def a(n):
    if n<= 1:
        return n
    else:
        return (n+a(n-1))
print(a(n=int(input('Enter a number: '))))

# Define a function which can generate and print a list where the values are square of numbers between 1 and 20
def printlst(a):
    l = []
    for i in range(1,a+1):
        l += [i**2]
    return l
print(printlst(20))

# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.
def printDic(n):
    d = {}
    for i in range(1,n+1):
        d[i]= i**2
        return d.keys()
print(printDic(n =int(input('Enter a number: '))))

# Write a function that count the no of characters of the given input text
def finput(n):
    b = n.split(' ')
    count = ''
    for i in b:
        print(i+ ':', len(i))
print(finput('innomatics research labs'))

# Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
l1 = [1,2,3,4,5,6,7,8,9]
print(list(map(lambda a: a**2,l1)))

# Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
l1 = [1,2,3,4,5,6,7]
a = list(filter(lambda x:(x % 2== 0),l1))
print(list(map(lambda x:x**2,a)))

# Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included)
def even(x):
    return list(filter(lambda a: a %2==0,x))
print(even(range(1,20)))