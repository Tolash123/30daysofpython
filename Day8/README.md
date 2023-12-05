# Day-8 of #30daysofPython

## List

Functions of a List
Methods of a List
Adding elements in a List
Removing elements in a List
Sorting a List

- - Ascending Order
- - Descending Order
Counting how many times an element is repeated.
Finding index of an element
Joining a list

### LIST
List is mutable, we can add and remove elements in a list.
List is represented as [ ]

#### Functions of a list:

len(list)------> Represents length of a list.
max(list)------> Gives maximum value in a list.
min(list)------> Gives minimum value in a list.
list()---------> converts any datatype into list.

### Methods in a list

- Adding elements in a list:
list.append() -----> Adds one element, by default it adds in last position
list.extend([ , ]) -----> Adds multiple elements, by default it adds in last position
list.insert(index,element) -----> Adds element at specifies index

#### Removing elements in a List:
list.remove()----------->Removes the element
list.pop(index)--------->Removes element based on index
list.clear()------------>Clears all the elements in a list
del list[index]--------->Removes element based on index

### Sorting List

- Sorting can be done by:
list.sort()
sorted(list)
Sorting in Ascending order

## Counting repeated elements in a list:

list.count() is used to count how many times an elements is repeated.