# Day-15 of #30daysofpython

## Strings Datatype Examples

1. Program to Reverse the given String

- Method-1 using Slice Operator
> a = input("Enter a String: ") print(a[::-1]) 

- Method-2 Using 'reversed()' function
> a = input("Enter a String: ") print(''.join(reversed(a)))

- Method-3 Using 'while' loop
a = input("Enter a String:")
i=len(a)-1
target=''
while i>=0:
    target=target+a[i]
    i=i-1
print(target)


