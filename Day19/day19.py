# Write a function that computes the volume of a sphere given its radius.
# volume = 4/3 pi r^3
def vol():
    import math as m
    rad = int(input('Enter the given radius: '))
    return (4/3)*m.pi*(rad**3)

print(vol())

# Write a function that checks whether a number is in a given range (Inclusive of high and low)
def ran_check(num,low,high):
    if num in range(low,high+1):
        print('{} is in range of {} & {}'.format(num,low,high))
    else: 
        print('{} is not range of {} & {}'.format(num,low,high))

ran_check(5,3,6)

# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def up_low(s):
    count = 0
    count1 = 0
    for i in s:
        if i.isupper():
            count +=1
    print('No of upper case characters: ',count)
    for i in s:
        if i.islower():
            count1 +=1
    print('No of lower case characters:  ', count1)

up_low('Hello Mr. Rogers, how are you this fine Tuesday?')

# Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(l):
    s = set(l)
    return list(s)
print(unique_list([1,2,3,4,54,2,1,2,1]))

# Write a Python function to multiply all the numbers in a list.
def multiply(num):
    count = 1
    for i in num:
        count *=i
    print(count)
multiply([1,2,3,-5])

