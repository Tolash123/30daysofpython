# set in python
a = {1,2,3,4,5,6,7,8,9}
print(type(a))

s = {'a','b','c','d','e','f','g','h'}
print(s)      #Unordered sequence
print(type(s))

# repeated numbers are not allowed
b = {1,2,2,2,4,5,6,7,8,9}
print(b)

# adding elements in sets using add() and update()

a = {1,2,3,4,5}
b = {'a','b','c'}
a.add(6)
a.update(b)
print(a)

# Removing elements from a setpop() , by default removes last index element

a = {1,2,3,4,5}
b = {'a','b','c'}
a.pop()
a.remove(3)
b.discard('a')
print(a)
print(b)
a.clear()
print(a)
a= b.copy()
print(a)

# difference(), union(), intersection()
a = {1,2,3,4,5,6}
b = {4,5,6,7,8,9}
c = a.difference(b) #Removes 'b' elements from 'a' & returns set 'a'
d = b.difference(a) #Removes 'a' elements from 'b' & returns set 'b'
print(c)
print(d)
e = a.intersection(b)
f = a.union(b)
print(e)

# #difference_update()
a = {1,2,3,4,5,6}
b = {4,5,6,7,8,9}
b.intersection_update(a)
a.difference_update(b) #Removes common elements in 'a' &' b' and returns 'a'
print(b)
print(a)

# issuperset() returns True if a set has every elements of another set else returns False
a = {1,2,3,4,5,6}
b = {4,5,6,7,8,9}
c= a.issuperset(b)
print(c)