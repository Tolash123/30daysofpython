# Day-3 of #30daysofPython

## Operators

- Continuation of Operators

Assignment
Terenary
Special Operators
Identity operator
Membership Operator
Operator Precedence
Mathematical functions by using math module

### Assignment Operator

Assigning values to a variables

1. +=
2. -=
3. /=
4. *=
5. //=
6. **=
7. &=
8. |=
9. ^=
10. >>=
11. <<=

## Terenary Operator

- Writing multiple statements in a single line
Examples
> a = 10
 b = 20
 c = a if a>b else b       # Here we are writing if, else in a single line
 print(c)

## Special Operators

### Identity Operator
is
is not

### Membership Operator
in
not in

## Operator Precedence

- Operator precedence says which need to be operate first

( )-------->Paranthesis
**--------->Exponential operator
~ --------->Bitwise Complementary
'*','/','%','//'--->Multiplication, Division, Modulo, Floor Division
'+','-' -----------> Addition, Subtraction
<<, >> ----------> Left shift and Right Shift
'&'--------------->Bitwise and
'^' --------------->Bitwise X-or
'|' ---------------->Bitwise or
>,>=,<,<=, ==, !=------> Relational and Equality operators
=,+=,-=,*= ---------------> Assignment operator
is, not is ----------------> Identity operators
in, not in ----------------> Membership operator
not , and, or------------------------> logical operators


### Mathematical functions from 'math' module

- This can be done in three ways

* import math
+ import math as m
+ from math import * #imports all elements in math module