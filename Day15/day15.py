# program to reverse the given string using slice, reverse and while loop
a = 'Dristol'
print(a[::-1])
print(''.join(reversed(a)))
# for while
a = 'Tolani'
i = len(a)-1
target = ''
while i>=0:
    target += a[i]
    i = i-1
    print(target)

# Program to Reverse Order of Words
a = input('Enter words to be reversed: ')
l = a.split()
l1 =[]
i = len(l)-1
while i>=0:
    l1.append(l[i])
    i=i-1
    output =' '.join(l1)
    print(output)

# Program to Reverse Internal Content of each Word

a = 'England is a developed country'
b = a.split()
b1 = []
i=0
while i<len(b):
    b1.append(b[i][::-1])
    i=i+1
    output= ' '.join(b1)
    print(output)

# Program to Print Characters at Odd Position and Even Position for a String?
a = input('Enter a string: ')
print('The character at even are: ',a[::2])
print('The character at even are: ',a[1::2])

# using while loop to do that
b = input('Enter your preferred words: ')
i=0
print('The character at even are: ')
while i<len(b):
    print(b[i], end='')
    i=i+2
print()
print('The character at odd are: ')
i=1
while i<len(b):
    print(b[i], end='')
    i=i+2
print()

# Program to merge Characters of 2 Strings into a Single String by Characters alternatively
a = 'Alade'
b = 'Idris'
output = ''
i,j=0,0
while i<len(a) or j<len(b):
    if i<len(a):
        output=output+a[i]
        i+=1
    if j<len(b):
        output=output+b[j]
        j+=1
print(output)

# Program to Sort the Characters of String & 1st Alphabet Symbols followed by Numeric Values
a=input("Enter a String:")
s1=s2=output=''
for x in a:
    if x.isalpha():
        s1=s1+x
    else:
        s2=s2+x
for x in sorted(s1):
    output=output+x
for x in sorted(s2):
    output=output+x
print(output)

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

# Program to find the number of Occurrences of each Character the String

s = input('Enter a string: ')
d = {}
for x in s:
    if x in d.keys():
        d[x]=d[x]+1
    else:
        d[x]=1
for a,b in d.items():
    print('{} = {} times'.format(a,b))

# Program to print: Output: 'one owt three ruof five xis seven' if
s = input('Enter a string: ')
l = s.split()
l1 = []
i = 0
while i<len(l):
    if i % 2==0:
        l1.append(l[i])
    else:
        l1.append(l[1][::-1])
    i=i+1
output = ' '.join(l1)
print('Original string: ', s)
print('Output string: ', output)