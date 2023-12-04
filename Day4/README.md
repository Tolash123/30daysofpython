# Day-4 of #30daysofPython

## Input Statements 

- input( )
- Reading multiple values from user
- Shortcut to read multiple values in a single line
- eval() function

### input( ) is a function that takes input from a user.
Examples
> a = input("Enter a word : ")
 print(a)
 print(type(a))

Note: input( ) function by default gives 'str' datatype.

### Shortcut to read multiple inputs in a single line
> a,b,c = [int(x) for x in input("Enter 3 numbers : ").split(',')]
  print("The sum of a,b,c is : ",a+b+c)