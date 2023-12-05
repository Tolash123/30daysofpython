# Day-9 of #30daysofPython

## Dictionaries

### Functions
#### Methods
- Adding elements in a dictionary
- Removing elements in a dictionary
- Displaying keys, values & items.

#### Functions

len(dict)------> Represents length of a dictionary.
str(dict)---------> converts dict datatype into string.
type(dict)--------> Returns type of dict.

##### len()
Example:
> dict1 = {1:'a',2:'b',3:'c',4:'d'} 
  len(dict1)

### Methods

Adding Elements in a Dictionary

dict1.update(dict2)---------> To add/append a dictionary
dict3 = {dict1,dict2}---> Combines two dictionaries.
Example:

> dict1 = {1:'a',2:'b',3:'c',4:'d'}
 dict2 = {5:'e',6:'f',7:'g',8:'h'}
 dict1.update(dict2)
 print(dict1)

- Removing Elements in a Dictionary
pop(2)-----------> removes key which has key as 2
del dict[3]------> removes key which has key as 3
clear()----------> Clears the dictionary completely
popitem()--------> Removes last inserted key-value pair

###### fromkeys()
We use fromkeys( ) when we have same values for different keys.