# tuple
a = ('alade','tolani')
print(type(a))

# dictionary
a = {1: 'milk', 2: 'biscuits'}
print(type(a))

# set
a = {'biscuits', 'milk'}
print(type(a))

# list
a = ['book', 'ball']
print(type(a))

# to convert tuple to list
b = ('book', 'bank', 'door')
c = list(b)
c.extend(['fish', 'bag'])
print(c)
print(type(c))

#With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.

t = (1,2,3,4,5,6,7,8,9,10)
t1 = t[0:5]
print(t1)
t2 = t[5:]
print(t2)

# Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10)
t = (1,2,3,4,5,6,7,8,9,10)
for i in t:
    if i % 2 == 0:
        print(i, end='')
print('\n')

# Write a program to generate and print another tuple whose values are odd numbers in the given tuple (1,2,3,4,5,6,7,8,9,10)
t = (1,2,3,4,5,6,7,8,9,10)
l = []
for i in t:
    if i % 2 == 1:
        l += [i]
        t1= tuple(l)
        print(t1, end='')
print('\n')