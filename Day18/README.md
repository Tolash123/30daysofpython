# Day-18 #30daysofpython

## Function
- def keyword
- simple example of a function
- calling a function with ()
- accepting parameters
- print versus return
- adding in logic inside a function
- multiple returns inside a function
- adding in loops inside a fuction
- interactions between functions
- lambda functions [map(), filter(), *args & *kwargs]

### Functions
def keyword
> def name_of_function(arg1,arg2):
     # Do stuff here
     # Return desireed result

> Example: def say_hello(): print('Hello')

#### Calling a function
say_hello()

### What is the difference between return and print?

The return keyword allows you to actually save the result of the output of a function as a variable. print() function simply displays the output to you, but doesn't save it for future use. 

### Interaction between functions

Functions often use results from other functions, let's see a simple example through a guessing game. there will be 3 positions in the list, one of which is an 'O', a function will shuffle the list, another will take a player's guess, and finally another will check to see if it is correct. This is based on the classic carnival game of guessing which cup a red ball is under.


#### Lambda Expressions 

- Map
- Filter