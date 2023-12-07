# Program to print output as 'abbcccddddeeeee' for input: Input: 'a1b2c3d4e5'
a = input('Enter a string: ')
output = ''
for x in a:
    if x.isalpha():
        output=output+x
        previous=x
    else:
        output=output+previous*(int(x)-1)
print(output)

# Program to remove Duplicate Characters from the given String?
s = input('Enter a string: ')
l = []
for x in s:
    if x not in l:
        l.append(x)
        output=''.join(l)
print(output)