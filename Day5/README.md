# Day-5 of #30daysofPython

## Output Statements

- print( ) statement
- end( ) attribute
- sep( ) attribute
- print statement with '{ }' Replacement operator
- print statement with formatted string

### print( ) statement

print( ) statement is used to print the output
print('a') # Since 'a' is string it prints 'a' but print(a) gives error if a is not initialised
 > a = 10 print(a)

### end() attribute
This attribute is used if we need the output in a single line.
Example
a =[10,20,30,40,50,60]
for i in a:
    print(i)

### sep( ) attribute

This attribute used to seperate two different outputs

Examples
> print('10','08','2021', sep='-')

### Using end( ) and sep( ) in a single line

> print(10,20,30,sep=':',end='!')

### print( ) statement with replacemenet operator {}

Examples
> a = 'Balaji'
 b = 'Hello'
 print("{} {}!,how are you?".format(a,b))